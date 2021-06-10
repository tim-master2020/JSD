from os import mkdir,rmdir
import os
from unipath import Path
from os.path import exists, dirname, join, isfile
from shutil import copy
import jinja2
from textx import metamodel_for_language, model as md
import datetime
import sys
from pprint import pprint
import re
# importing shutil module
import shutil

def generate(model, output_path, overwrite):

    now = datetime.datetime.now().strftime("%a, %b %d, %Y %X")
    this_folder = dirname(__file__)

    if not exists(output_path):
        mkdir(output_path)
    # create output folders
    output_folder = join(output_path, 'generator_output')

    if not overwrite and exists(output_folder):
        print('-- Skipping: {}'.format(output_folder))
        return
    if not exists(output_folder):
        mkdir(output_folder)



    ##########################################################################################################
    #BackEnd generator
    ##########################################################################################################
    p = Path(output_path)
    if exists(join(output_folder, 'backend')):
        shutil.rmtree(join(output_folder, 'backend'))
        
    backend_demo_f =  join(output_folder, 'backend','demo')
    shutil.copytree(join(p.parent, 'demo'),  backend_demo_f)

    print('output folder at top'+str(output_folder))

    backendGeneratedFolder = generateBackendStructure(output_folder,'generated')
    print('backendGeneratedFolder'+str(backendGeneratedFolder))

    output_folder_be_generated = backendGeneratedFolder
    backend_model_folder_repository_generated = join(output_folder_be_generated, 'repository')
    backend_model_service_generated = join(output_folder_be_generated, 'service')
    backend_model_controller_generated = join(output_folder_be_generated, 'controller')

    backendFolderDemo = generateBackendStructure(output_folder,'demo')
    print('backendFolderDemo'+str(backendFolderDemo))

    output_folder_be = backendFolderDemo
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

    if not exists(output_folder_be_generated):
        mkdir(output_folder_be_generated)

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

    ##########################################################################################################
    #Frontent generator

    frontend_folder = join(output_folder, 'front')
    if exists(frontend_folder):
        shutil.rmtree(frontend_folder)
    shutil.copytree(join(p.parent, 'front'), join(output_folder, 'front'))


    frontend_angular = generateFrontendFolderStructure(frontend_folder,'app')
    frontend_angular_generated = generateFrontendFolderStructure(frontend_folder,'generated')
    if not exists(frontend_angular_generated):
        mkdir(frontend_angular_generated)
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

def generateBackendStructure(output_folder,depth):
    backend = join(output_folder,'backend')
    backend_demo = join(backend,'demo')
    backend_demo_src = join(backend_demo,'src')
    backend_demo_src_main = join(backend_demo_src,'main')
    backend_demo_src_main_java = join(backend_demo_src_main,'java')
    backend_demo_src_main_java_com = join(backend_demo_src_main_java,'com')
    backend_demo_src_main_java_com_example = join(backend_demo_src_main_java_com,'example')
    backend_demo_src_main_java_com_example_demo = join(backend_demo_src_main_java_com_example,'demo')

    if depth == 'generated':
        backend_demo_src_main_java_com_example_demo_generated = join(backend_demo_src_main_java_com_example_demo,'generated')
        return backend_demo_src_main_java_com_example_demo_generated
    else:
        return backend_demo_src_main_java_com_example_demo


def generateFrontendFolderStructure(output_folder,depth):

    angularFront = join(output_folder,'AngularFront');
    angularFront_src = join(angularFront,'src');
    angularFront_src_app = join(angularFront_src,'app');
    if depth == 'generated':
        return join(angularFront_src_app,'generated')
    else:
        return angularFront_src_app

    #AngularFront/src/app


