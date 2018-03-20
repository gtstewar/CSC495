class BaseObject(object):
    """The basic object for csc 495 project."""
    def __methods__(self):
        """Show methods for the class"""
        return '\n'.join([i for i in sorted(type(self).__dict__)
                          if i[0] is not '_'])

    def __repr__(self):
        """Class, Show your identity!"""
        information = "name: " + self.__class__.__name__
        if self.__doc__ is not None:
            information += "\n" + self.__doc__
        if self.__methods__().__len__() != 0:
            information += "\n" + "available methods: "
            information += "\n" + self.__methods__()
        return information
