
class SParam:
    """
    Class for storing parameters for use in a SUSF project.

    Usage:
        In a module's __init__(self) function you can use any of the 
        load_params_from_* functions to load the module's parameters into an 
        object member of the class, for example:

            self.params = load_params_from_hjson('mod_params.hjson')

        self.params will be an object with the same structure as the parameter 
        file, so you can access members such as self.params.a.b.
    """

    @classmethod
    def from_dict(cls, dict):
        """
        Internal function used to hook into the x.loads function. Do not use 
        this function, instead use one of the load_params_from_* functions.

        Matches the function definition for an object_hook.
        """
        obj = cls()
        obj.__dict__.update(dict)
        obj.raw = dict
        return obj