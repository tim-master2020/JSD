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
    if property.type.name not in ['integer', 'string','boolean','float'] and property.annotiation is None:
        raise TextXSemanticError('Annotation must be written for model type!')
    
    #Check if right annotations are used

    if property.annotiation in ['@OneToMany','@ManyToMany'] and property.objectType is None:
        raise TextXSemanticError('attribute type should be a container!',property.annotiation)

    if property.annotiation in ['@OneToOne','@ManyToOne'] and property.objectType is not None:
        raise TextXSemanticError('attribute type should not be a container!',property.annotiation)

    if property.type.name in ['integer', 'string','boolean','float'] and property.objectType in ['ArrayList','HashMap','HashSet','[]'] and property.annotiation is not None:
        raise TextXSemanticError("Current version of this language doesn't support mixing primitive values with given data structures! Try with type that you have already defined as one of the models. ")
    
    property.primitive = property.type.name  in ['integer', 'string','boolean','float']
    property.isArray = property.objectType == '[]'
    property.isArrayList = property.objectType == 'ArrayList'
    property.isSet = property.objectType == 'HashSet'

    if property.type.name in ['integer', 'string','boolean','float'] and property.objectType in ['ArrayList','HashMap','HashSet','[]'] and property.annotiation is not None:
        raise TextXSemanticError("Current version of this language doesn't support mixing primitive values with given data structures! Try with type that you have already defined as one of the models. ")

    property.primitve = property.type.name  in ['integer', 'string','boolean','float']
    property.isArray = property.objectType == '[]'
    property.isArrayList = property.objectType == 'ArrayList'
    property.isSet = property.objectType == 'HashSet'

def get_meta_model():

    # build metamodel
    current_dir = os.path.dirname(__file__)

    grammar_path = os.path.join(current_dir, 'Java.tx')

    object_processors = {
        'Property': property_type_processor
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

