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
        """  # TODO refactor this.
        self._double_value = float(value)

    @staticmethod
    def get_value(argument_marshaler):
        """
        Return the double value of the argument marshaler object passed to it.
        :param argument_marshaler: DoubleMarshaler.
        :return:
        """
        return argument_marshaler._double_value
