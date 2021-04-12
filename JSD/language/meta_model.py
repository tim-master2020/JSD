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
    # print(property.objectType)
    # print(property.type.name)
    # print(property.propName)
    # print('-----------')
    property.primitive = property.type.name  in ['integer', 'string','boolean','float']
    property.isArray = property.objectType == '[]'
    property.isSet = property.objectType == '{}'
    property.annotation = '@Column'

    # if property.type.name not in ['integer', 'string','boolean','float'] and property.objectType is None and property.propName is None:
    #     property.annotation = '@OneToOne'
        

def model_type_processor(model):   
    properties = list(map(lambda x: x.name, model.properties))
    for p in properties:
        if(properties.count(p) > 1):
            raise TextXSemanticError("Model can't have same property names.")

def app_type_processor(app):
    print('////app/////')

    for model in app.models:

        for prop in model.properties:
            print('------')

            if prop.annotation is '@Column' and prop.type.name not in ['integer', 'string','boolean','float']:
                if prop.objectType is None and prop.propName is None:
                    prop.annotation = '@OneToOne'
                
                if prop.propName is not None:
                    print('Refereced model:')
                    print(prop.propName)
                    referenced_model = next((x for x in app.models if x.name == prop.type.name), None)
                    referenced_prop = next((x for x in referenced_model.properties if x.name == prop.propName.name), None)

                    if referenced_prop is None:
                        raise TextXSemanticError("Property {} is referencing a non-existent property name in model {}.".format(prop.propName.name, referenced_model.name))
                    
                    if prop.objectType is None:
                        
                        if referenced_prop.objectType is None:
                            raise TextXSemanticError("Property {} is referencing an invalid property name in model {}. It must referece a collection.".format(prop.propName.name, referenced_model.name))
                        else:
                            prop.annotation = '@ManyToOne\n' + '\t@JoinColumn(name = "{}_id")'.format(referenced_prop.name)
                            referenced_prop.annotation = '@OneToMany(fetch = FetchType.LAZY, mappedBy = "{}")'.format(prop.name)
                            
                    else:
                        if referenced_prop.objectType is not None:
                            prop.annotation = '@ManyToMany(mappedBy = "{}", fetch = FetchType.EAGER)'.format(referenced_prop.name)
                            referenced_prop.annotation = '@ManyToMany'
                        else:
                            prop.annotation = '@OneToMany(fetch = FetchType.LAZY, mappedBy = {}")'.format.prop_name
                            referenced_prop.annotation = '@ManyToOne\n' + '\t@JoinColumn(name = "{}_id")'.format(prop.name)
                elif prop.objectType is not None:
                    raise TextXSemanticError("Property {} must provide referenced property's name.".format(prop.name))
                        



                    



def get_meta_model():

    # build metamodel
    current_dir = os.path.dirname(__file__)

    grammar_path = os.path.join(current_dir, 'Java.tx')

    object_processors = {
        'Property': property_type_processor,
        'Model' : model_type_processor,
        'App' : app_type_processor
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

