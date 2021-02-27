from os.path import dirname, join
from textx import language as lang
from textx import generator as gen
from .generator.generator import generate

from .language.meta_model import get_meta_model
from .generator.generator import generate

@lang('JSD','*.jsb')
def java_spring_boot_lang():

    return get_meta_model()

@gen('JSD', 'java+html+js')
def java_spring_boot_gen(metamodel, model, output_path, overwrite, debug):
    """
    Generating web-based spring boot application and angular application
    """
    input_file = model._tx_filename
    outuput_dir = output_path if output_path else dirname(input_file)

    generate(model, outuput_dir, overwrite)



    