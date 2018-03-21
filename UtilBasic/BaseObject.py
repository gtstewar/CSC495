from itertools import chain


class BaseObject(object):
    """The basic object for csc 495 project."""
    def __methods__(self):
        """Show methods for the class in list"""
        return [i for i in sorted(type(self).__dict__)
                if not str(i).startswith('_')]

    def __repr__(self):
        """
        Class, Show your identity!
        Mainly three parts: doc, methods, attributes
        """
        information = ["name: " + self.__class__.__name__]
        if self.__doc__ is not None:
            information.append("---")
            information.append("available document: ")
            information += self.__doc__.split('\n')
        if self.__methods__().__len__() != 0:
            information.append("---")
            information.append("available methods: ")
            information += self.__methods__()
        if self.__dict__ is not None:
            information.append("---")
            information.append("attributes: ")
            local_temp = ["====================\n" +
                          i + " -> " + str(self.__dict__[i])
                          for i in sorted(self.__dict__)]
            local_temp = list(chain.from_iterable(map(lambda x: x.split('\n'),
                                                      local_temp)))
            local_temp = ["    " + i for i in local_temp]
            information += local_temp
        return '\n'.join(information)
