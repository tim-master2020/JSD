from textx import metamodel_from_file
import os
from textx import metamodel_from_file, TextXSyntaxError, TextXSemanticError

class Model(object):
    def __init__(self,parent ,name, properties, controller,dependencies):
        self.parent = parent
        self.name = name
        self.properties = properties
        self.controller = controller
        self.dependencies = dependencies

class Property(object):
    def __init__(self, parent,prop_name, value):
        self.parent = parent
        self.prop_name = prop_name
        self.value = value

    def __str__(self):
        return self.prop_name


def property_type_processor(property):
    """Checks if model type property has annotation."""
    
    if property.type.name in ['integer', 'string','boolean','float'] and property.objectType is '[]':
        raise TextXSemanticError("Current version of this language doesn't support mixing primitive values with given data structures! Try with type that you have already defined as one of the models. ")
    
    property.primitive = property.type.name  in ['integer', 'string','boolean','float']
    property.isArray = property.objectType == '[]'
    property.isSet = property.objectType == '{}'
    property.annotation = '@ManyToMany'

def model_type_processor(model):   
    properties = list(map(lambda x: x.name, model.properties))
    for p in properties:
        if(properties.count(p) > 1):
            raise TextXSemanticError("Model can't have same property names.")
   
def get_meta_model():

    # build metamodel
    current_dir = os.path.dirname(__file__)

    grammar_path = os.path.join(current_dir, 'Java.tx')

    object_processors = {
        'Property': property_type_processor,
        'Model' : model_type_processor,
    }

    model_builtins = {
        'integer': Model(None, 'integer', [],None,None),
        'string': Model(None, 'string', [],None,None),
        'float': Model(None, 'float', [],None,None),
        'boolean' : Model(None,'boolean',[],None,None)
    }

    metamodel = metamodel_from_file(grammar_path,classes=[Model],builtins=model_builtins)

    metamodel.register_obj_processors(object_processors)
    
    return metamodel

