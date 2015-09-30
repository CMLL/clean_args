__author__ = 'cllamach'


class StringListMarshaler(object):
    """
    Marshaler object to handle list of arguments.
    """

    def __init__(self):
        self._list_value = []

    def set(self, argument):
        """
        Set the value to the marshaler private list value.
        :param argument:
        :return:
        """
        self._list_value = argument.split(self._get_separating_letter(argument))

    def _get_separating_letter(self, argument):
        """
        Return the char that separates words in argument
        :param argument: String
        :return:
        """
        return ',' if ',' in argument else ' '

    @staticmethod
    def get_value(argument_marshaler):
        """
        Return the value of the passed argument marshaler.
        :param argument_marshaler: StringListMarshaler
        :return:
        """
        return argument_marshaler and argument_marshaler._list_value or []

