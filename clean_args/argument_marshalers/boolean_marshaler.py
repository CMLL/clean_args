__author__ = 'cllamach'


class BooleanMarshaler(object):
    """
    Boolean marshaler object to handle values passed as True flags.
    """

    def __init__(self):
        self._boolean_value = False

    def set(self, value):
        """
        Setter method for updating the value to True.
        :param value: String, param not used for boolean marshalers.
        :return:
        """
        self._boolean_value = True

    @staticmethod
    def get_value(argument_marshaler):
        """
        Return the boolean value of the passed marshaler.
        :param argument_marshaler:
        :return:
        """
        if isinstance(argument_marshaler, BooleanMarshaler):
            return argument_marshaler._boolean_value
