from clean_args.args_exception import ArgsException

__author__ = 'cllamach'


class DoubleMarshaler(object):
    """
    Marshaler object to handle double objects.
    """

    def __init__(self):
        self._double_value = None

    def set(self, value):
        """
        Set the double value.
        :param value: String
        :return:
        """
        try:
            self._double_value = float(value)
        except (ValueError, TypeError):
            raise ArgsException('Expected double value but got {}.'.format(
                value
            ))

    @staticmethod
    def get_value(argument_marshaler):
        """
        Return the double value of the argument marshaler object passed to it.
        :param argument_marshaler: DoubleMarshaler.
        :return:
        """
        if argument_marshaler:
            return argument_marshaler._double_value
        else:
            return 0.0