from textx import metamodel_from_file
import os
from textx import metamodel_from_file, TextXSyntaxError, TextXSemanticError

class Model(object):
    def __init__(self, name, properties, controller, implements, extends, template_path):
        self.name = name
        self.properties = properties
        self.controller = controller
        self.implements = implements
        self.extends = extends
        self.template_path = template_path

    def __str__(self):
        return self.name

class Property(object):
    def __init__(self, prop_name, value):
        self.prop_name = prop_name
        self.value = value

    def __str__(self):
        return self.prop_name


def model_type_processor(properties):
    """Checks if model type property has annotation."""
    print(properties.prop_name_model_annotiation)
    if '' in properties.prop_name_model_annotiation:
        raise TextXSemanticError('Annotation must be written for model type!')


def get_meta_model():

    # build metamodel
    current_dir = os.path.dirname(__file__)

    grammar_path = os.path.join(current_dir, 'Java.tx')

    object_processors = {
        'Property': model_type_processor
    }

    metamodel = metamodel_from_file(grammar_path)

    metamodel.register_obj_processors(object_processors)
    
    return metamodel

