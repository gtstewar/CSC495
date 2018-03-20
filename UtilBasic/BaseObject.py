class BaseObject(object):
    """The basic object for csc 495 project."""
    def __methods__(self):
        """Show methods for the class"""
        return '\n'.join([i + ":\n" + i.__doc__ + "\n"
                          for i in sorted(self.__dict__.keys())
                          if i[0] is not '_'])

    def __repr__(self):
        """Class, Show your identity!"""
        return "name: " + self.__class__.__name__ + "\n" + self.__methods__()
