from .sparam import SParam
import hjson

def load_params_from_hjson(file_path_in):
    """
    Load a parameter HJSON file into an object.

    Usage:
        params = load_params_from_hjson(absolute_path_to_params_file)
    """

    # Open the parameter file
    with open(file_path_in, mode='r') as param_file:
        # Convert the file into an object using the object_hook trick from here:
        # https://stackoverflow.com/questions/43776223/converting-nested-json-into-python-object
        params = hjson.loads(param_file.read(), object_hook=SParam.from_dict)

    return params

