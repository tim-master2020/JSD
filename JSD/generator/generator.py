from os import mkdir
from os.path import exists, dirname, join
from shutil import copy
import jinja2
from textx import metamodel_for_language, model as md
import datetime
import sys
from pprint import pprint

def generate(model, output_path, overwrite):
    """
    Generates spring boot backend + angular frontend applications for  domain specific language
    Parameters: 
        model (Survey): textX model that represents the survey
        output_path (string): The output to generate to
        overwrite (boolean): Should overwrite output files 
    """

    now = datetime.datetime.now().strftime("%a, %b %d, %Y %X")
    this_folder = dirname(__file__)
    # create output folders
    output_folder = join(output_path, 'generator_output/')
    if not overwrite and exists(output_folder):
        print('-- Skipping: {}'.format(output_folder))
        return
    if not exists(output_folder):
        mkdir(output_folder)



    ##########################################################################################################
    #BackEnd generator
    ##########################################################################################################
    backend_folder = join(output_folder, 'backend/')
    backend_model = join(backend_folder, 'model')
    backend_model_folder_repository = join(backend_folder, 'repository')
    backend_model_service = join(backend_folder, 'service')

    if not exists(backend_folder):
        mkdir(backend_folder)

    if not exists(backend_model):
        mkdir(backend_model)

    if not exists(backend_model_folder_repository):
        mkdir(backend_model_folder_repository)

    if not exists(backend_model_service):
        mkdir(backend_model_service)

    
    models  = md.get_children_of_type("Model", model)
    models = set(models)
    print('models',models)
    
      

        # if(model.controller)
        #     if not exists(join(backend_folder,'controller')):
        #         backend_model_controller = join(backend_folder, 'controller')
        #         mkdir(backend_model_controller)
          
    
    # initialize template engine
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(join(this_folder, 'templates')),
        trim_blocks=True,
        lstrip_blocks=True)

    template = jinja_env.get_template('model_backend.j2')
    templateIService = jinja_env.get_template('model_iservice.j2')
    templateService = jinja_env.get_template('model_service.j2')

    #kreairanje modela u model folderu
    for model in models:
        f = open(join(backend_model, "%s.java" % model.name), 'w')
        f.write(template.render(model=model, datetime=now))

        s = open(join(backend_model_service, "I%sService.java" % model.name), 'w')
        s.write(templateIService.render(model=model, datetime=now))

        ss = open(join(backend_model_service, "%sService.java" % model.name), 'w')
        ss.write(templateService.render(model=model, datetime=now))

        if(model.property):
            pprint(vars(model.property))

    ##########################################################################################################
    #Frontent generator
    ##########################################################################################################

    frontend_folder = join(output_folder, 'front/')
    if not exists(frontend_folder):
        mkdir(frontend_folder)

    frontend_angular = join(frontend_folder, 'AngularFront/src/app')
    frontend_angular_setings = join(frontend_folder, 'AngularFront')

    template = jinja_env.get_template('appComponent.j2')
    f = open(join(frontend_angular, "app.component.html"), 'w')
    f.write(template.render(model=model, datetime=now))

    template = jinja_env.get_template('appModule.j2')
    f = open(join(frontend_angular, "app.module.ts"), 'w')
    f.write(template.render(models=models, datetime=now))

    template = jinja_env.get_template('appRouting.j2')
    f = open(join(frontend_angular, "app-routing.module.ts"), 'w')
    f.write(template.render(models=models, datetime=now))

    template = jinja_env.get_template('angularJson.j2')
    f = open(join(frontend_angular_setings, "angular.json"), 'w')
    f.write(template.render(models=models, datetime=now))

    component_folder_home = join(frontend_angular,"Home")
    if not exists(component_folder_home):
            mkdir(component_folder_home)
            
    template = jinja_env.get_template('homeTs.j2')
    f = open(join(component_folder_home, "Home.ts"), 'w')
    f.write(template.render(models=models, datetime=now))

    template = jinja_env.get_template('homeHtml.j2')
    f = open(join(component_folder_home, "Home.html"), 'w')
    f.write(template.render(models=models, datetime=now))

    template = jinja_env.get_template('service.j2')
    f = open(join(frontend_angular, "app.service.ts"), 'w')
    f.write(template.render(models=models, datetime=now))

    for model in models:
        component_folder = join(frontend_angular,str(model.name))
        if not exists(component_folder):
            mkdir(component_folder)

        template = jinja_env.get_template('addTypescript.j2')
        f = open(join(component_folder, "%s.ts" % model.name), 'w')
        f.write(template.render(model=model, datetime=now))

        template = jinja_env.get_template('addHtml.j2')
        f = open(join(component_folder, "%s.html" % model.name), 'w')
        f.write(template.render(model=model, datetime=now))

        

 

    
    #kreairanje modela u model folderu
   

    # js_template = jinja_env.get_template('survey_js.j2')

    # f = open(join(js_output_folder, 'index.js'), 'w')
    # f.write(js_template.render(survey=model.survey, datetime=now))

    # copy(join(this_folder, 'templates/styles.css'), css_output_folder)
   
if __name__ == "__main__":

    this_folder = dirname(__file__)
    
    if len(sys.argv) < 2:
        print('Error: JavaSpringBootLan file is missing.')
    else:
        javaspringbootlan_file = sys.argv[1]

        javaspringboot_meta_model = metamodel_for_language('JSD')

        # build model
        model = survey_metamodel.model_from_file(javaspringbootlan_file)

        generate(model, this_folder, True)
