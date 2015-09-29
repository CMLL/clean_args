from clean_args.args_exception import ArgsException

__author__ = 'cllamach'


class StringMarshaler(object):
    """
    String marshaler object to handle the value passed as argument.
    """

    def __init__(self):
        self._string_value = ""

    def set(self, value):
        """
        Set the value passed as argument in the class.
        :param value: String
        :return:
        """
        if value:
            self._string_value = value
        else:
            raise ArgsException('Expected string but found {}.'.format(value))

    @staticmethod
    def get_value(argument_marshaler):
        """
        Return the value in the static marshaler object.
        :param argument_marshaler:
        :return:
        """
        return argument_marshaler._string_value

