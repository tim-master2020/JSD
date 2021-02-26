from textx import metamodel_from_file

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

def get_meta_model():

    current_dir = os.path.dirname(__file__)

    path = os.path.join(current_dir, 'JavaSpring.tx')

    # build metamodel
    metamodel = metamodel_from_file(path, classes=[Model])
    
    return metamodel