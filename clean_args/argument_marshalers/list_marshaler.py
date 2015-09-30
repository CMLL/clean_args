__author__ = 'cllamach'


class StringListMarshaler(object):
    """
    Marshaler object to handle list of arguments.
    """

    def __init__(self):
        self._list_value = []

    def set(self, value):
        """
        Set the value to the marshaler private list value.
        :param value:
        :return:
        """
        self._list_value = value.split(' ')

    @staticmethod
    def get_value(argument_marshaler):
        """
        Return the value of the passed argument marshaler.
        :param argument_marshaler: StringListMarshaler
        :return:
        """
        return argument_marshaler._list_value

