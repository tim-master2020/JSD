from os import mkdir
import os
from os.path import exists, dirname, join, isfile
from shutil import copy
import jinja2
from textx import metamodel_for_language, model as md
import datetime
import sys
from pprint import pprint
import re

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

    output_folder_be_generated = join(output_folder, 'backend/demo/src/main/java/com/example/demo/generated')
    backend_model_folder_repository_generated = join(output_folder_be_generated, 'repository')
    backend_model_service_generated = join(output_folder_be_generated, 'service')
    backend_model_controller_generated = join(output_folder_be_generated, 'controller')

    output_folder_be = join(output_folder, 'backend/demo/src/main/java/com/example/demo/')
    backend_model = join(output_folder_be, 'model')
    backend_model_folder_repository = join(output_folder_be, 'repository')
    backend_model_service = join(output_folder_be, 'service')
    backend_model_dto = join(output_folder_be, 'dto')
    backend_model_controller = join(output_folder_be, 'controller')

    if not exists(backend_model):
        mkdir(backend_model)

    if not exists(backend_model_folder_repository):
        mkdir(backend_model_folder_repository)

    if not exists(backend_model_service):
        mkdir(backend_model_service)

    if not exists(backend_model_dto):
        mkdir(backend_model_dto)
    
    if not exists(backend_model_controller):
        mkdir(backend_model_controller)

    if not exists(backend_model_folder_repository_generated):
        mkdir(backend_model_folder_repository_generated)

    if not exists(backend_model_service_generated):
        mkdir(backend_model_service_generated)
    
    if not exists(backend_model_controller_generated):
        mkdir(backend_model_controller_generated)

    
    models  = md.get_children_of_type("Model", model)
    models = set(models)
    print('models',models)
        
    def javatype(s):
        """
        Maps type names from PrimitiveType to Java.
        """
        return {
            'string': 'String',
            'integer': 'int'
        }.get(s, s)

    
    # initialize template engine
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(join(this_folder, 'templates')),
        trim_blocks=True,
        lstrip_blocks=True)

    jinja_env.filters['javatype'] = javatype
    template = jinja_env.get_template('model_backend_template.j2')
    templateIService = jinja_env.get_template('model_iservice.j2')
    templateGeneratedIService = jinja_env.get_template('modelGenerated_iservice.j2')
    templateService = jinja_env.get_template('model_service.j2')
    templateServiceGenerated = jinja_env.get_template('modelGenerated_service.j2')
    templateRepo = jinja_env.get_template('repository_backend.j2')
    templateRepoGenerated = jinja_env.get_template('repositoryGenerated_backend.j2')
    templateController = jinja_env.get_template('model_controller.j2')
    templateGeneratedController = jinja_env.get_template('modelGenerated_controller.j2')
    templateDto = jinja_env.get_template('dtoTemplate.j2')

    transferDTO = jinja_env.get_template('transferDTO.j2')
    s = open(join(backend_model_dto, "TransferDTO.java"), 'w')
    s.write(transferDTO.render(datetime=now))

    #kreairanje modela u model folderu
    for model in models:

        if not isfile(join(backend_model, "%s.java" % model.name)):
            f = open(join(backend_model, "%s.java" % model.name), 'w')
            f.write(template.render(model=model, datetime=now))

        if not isfile(join(backend_model_service, "I%sService.java" % model.name)):
            s = open(join(backend_model_service, "I%sService.java" % model.name), 'w')
            s.write(templateIService.render(model=model, datetime=now))

        s = open(join(backend_model_service_generated, "I%sGeneratedService.java" % model.name), 'w')
        s.write(templateGeneratedIService.render(model=model, datetime=now))

        if not isfile(join(backend_model_service, "%sService.java" % model.name)):
            ss = open(join(backend_model_service, "%sService.java" % model.name), 'w')
            ss.write(templateService.render(model=model, datetime=now))

        ss = open(join(backend_model_service_generated, "%sGeneratedService.java" % model.name), 'w')
        ss.write(templateServiceGenerated.render(model=model, datetime=now))

        if not isfile(join(backend_model_folder_repository, "%sRepository.java" % model.name)):
            ss = open(join(backend_model_folder_repository, "%sRepository.java" % model.name), 'w')
            ss.write(templateRepo.render(model=model, datetime=now))

        ss = open(join(backend_model_folder_repository_generated, "%sGeneratedRepository.java" % model.name), 'w')
        ss.write(templateRepoGenerated.render(model=model, datetime=now))
        s = open(join(backend_model_dto, "%sDTO.java" % model.name), 'w')
        s.write(templateDto.render(model=model, datetime=now))

        ss = open(join(backend_model_service, "%sService.java" % model.name), 'w')
        ss.write(templateService.render(model=model, datetime=now))

        if not isfile(join(backend_model_controller, "%sController.java" % model.name)):
            ss = open(join(backend_model_controller, "%sController.java" % model.name), 'w')
            ss.write(templateController.render(model=model, datetime=now))

        ss = open(join(backend_model_controller_generated, "%sGeneratedController.java" % model.name), 'w')
        ss.write(templateGeneratedController.render(model=model, datetime=now))

        # if(model.properties):
        #     for p in model.properties:
        #         print('property type is',p.type.name)
        #         print('property type', p.annotiation)
        #         print('property primitive : ', p.primitive)

    ##########################################################################################################
    #Frontent generator
    ##########################################################################################################

    frontend_folder = join(output_folder, 'front/')
    if not exists(frontend_folder):
        mkdir(frontend_folder)


    frontend_angular = join(frontend_folder, 'AngularFront/src/app/')
    frontend_angular_generated = join(frontend_folder, 'AngularFront/src/app/generated/')
    if not exists(frontend_angular_generated):
        mkdir(frontend_angular_generated)
    frontend_angular_setings = join(frontend_folder, 'AngularFront/')

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

    component_folder_home_generated = join(frontend_angular_generated,"home-generated")
    if not exists(component_folder_home_generated):
            mkdir(component_folder_home_generated)
    component_folder_home = join(frontend_angular,"home")
    if not exists(component_folder_home):
            mkdir(component_folder_home)
            
    template = jinja_env.get_template('homeGeneratedTs.j2')
    f = open(join(component_folder_home_generated, "HomeGenerated.ts"), 'w')
    f.write(template.render(models=models, datetime=now))

    if not isfile(join(component_folder_home, "Home.ts")):
        template = jinja_env.get_template('homeTs.j2')
        f = open(join(component_folder_home, "Home.ts"), 'w')
        f.write(template.render(models=models, datetime=now))


    template = jinja_env.get_template('homeGeneratedHtml.j2')
    f = open(join(component_folder_home_generated, "HomeGenerated.html"), 'w')
    f.write(template.render(models=models, datetime=now))

    template = jinja_env.get_template('serviceGenerated.j2')
    f = open(join(frontend_angular_generated, "appGenerated.service.ts"), 'w')
    f.write(template.render(models=models, datetime=now))

    if not isfile(join(frontend_angular, "app.service.ts")):
        template = jinja_env.get_template('service.j2')
        f = open(join(frontend_angular, "app.service.ts"), 'w')
        f.write(template.render(models=models, datetime=now))

    for model in models:
        component_folder_generated = join(frontend_angular_generated,str(model.name.lower()) + "-generated")
        if not exists(component_folder_generated):
            mkdir(component_folder_generated)
        component_folder = join(frontend_angular,str(model.name))
        if not exists(component_folder):
            mkdir(component_folder)

        template = jinja_env.get_template('addTypescriptGenerated.j2')
        f = open(join(component_folder_generated, "%sGenerated.ts" % model.name), 'w')
        f.write(template.render(model=model, models=models, datetime=now))

        if not isfile(join(component_folder, "%s.ts" % model.name)):
            template = jinja_env.get_template('addTypescript.j2')
            f = open(join(component_folder, "%s.ts" % model.name), 'w')
            f.write(template.render(model=model, models=models, datetime=now))

        template = jinja_env.get_template('previewTypescriptGenerated.j2')
        f = open(join(component_folder_generated, "%sPreviewGenerated.ts" % model.name), 'w')
        f.write(template.render(model=model, models=models, datetime=now))

        if not isfile(join(component_folder, "%sPreview.ts" % model.name)):
            template = jinja_env.get_template('previewTypescript.j2')
            f = open(join(component_folder, "%sPreview.ts" % model.name), 'w')
            f.write(template.render(model=model, models=models, datetime=now))

        template = jinja_env.get_template('editTypescriptGenerated.j2')
        f = open(join(component_folder_generated, "%sEditGenerated.ts" % model.name), 'w')
        f.write(template.render(model=model, models=models, datetime=now))

        if not isfile(join(component_folder, "%sEdit.ts" % model.name)):
            template = jinja_env.get_template('editTypescript.j2')
            f = open(join(component_folder, "%sEdit.ts" % model.name), 'w')
            f.write(template.render(model=model, models=models, datetime=now))

        template = jinja_env.get_template('addHtml.j2')
        f = open(join(component_folder_generated, "%sGenerated.html" % model.name), 'w')
        f.write(template.render(model=model, models=models, datetime=now))

        template = jinja_env.get_template('previewModel.j2')
        f = open(join(component_folder_generated, "%sPreviewGenerated.html" % model.name), 'w')
        f.write(template.render(model=model, models=models, datetime=now))

        template = jinja_env.get_template('editHtml.j2')
        f = open(join(component_folder_generated, "%sEditGenerated.html" % model.name), 'w')
        f.write(template.render(model=model, models=models, datetime=now))


        

 

    
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
