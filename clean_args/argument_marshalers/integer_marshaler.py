from clean_args.args_exception import ArgsException
__author__ = 'cllamach'


class IntegerMarshaler(object):
    """
    Integer class for handling values.
    """

    def __init__(self):
        self._integer_value = None

    def set(self, value):
        """
        Setter method to update the value.
        :param value: String, value passed via arguments.
        :return:
        """
        try:
            self._integer_value = int(value)
        except ValueError:
            raise ArgsException('Expected integer but got {}.'.format(value))

    @staticmethod
    def get_value(argument_marshaler):
        """
        Extract the integer value from the marshaler.
        :param argument_marshaler: IntegerArgumentMarshaler.
        :return:
        """
        return argument_marshaler._integer_value
