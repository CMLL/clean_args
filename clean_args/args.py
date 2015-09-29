from clean_args.args_exception import ArgsException
from argument_marshalers.boolean_marshaler import BooleanMarshaler
from argument_marshalers.integer_marshaler import IntegerMarshaler
from clean_args.argument_marshalers.DoubleMarshaler import DoubleMarshaler
from clean_args.argument_marshalers.string_marshaler import StringMarshaler

__author__ = 'cllamach'


class CleanArgs(object):
    """
    Argument handler class.
    """

    def __init__(self, schema, args):
        """
        Constructor for class, parses schema and arguments based on
        said schema.
        :param schema: String, configuration for the passed arguments.
        :param args: List, arguments to parse.
        :return:
        """
        self._schema = schema
        self._args = args
        self._arguments = {}
        self._current_argument = None
        self._parse_schema()
        self._parse_argument_list()

    def _parse_schema(self):
        """
        Parse the schema according to its content.
        :return:
        """
        schema_elements = self._schema.split(',')
        for element in schema_elements:
            self._parse_schema_element(element)

    def _parse_schema_element(self, element):
        """
        Classify the element according to its nature.
        :param element: String, element to classify.
        :return:
        """
        element_id = element[0]
        element_tail = element[1:]
        self._validate_schema_element_id(element_id)
        if not element_tail:
            self._arguments.update({element_id: BooleanMarshaler()})
        elif element_tail == '*':
            self._arguments.update({element_id: IntegerMarshaler()})
        elif element_tail == '#':
            self._arguments.update({element_id: StringMarshaler()})
        elif element_tail == '##':
            self._arguments.update({element_id: DoubleMarshaler()})
        else:
            raise ArgsException('{} is not a valid schema value.'.format(
                element_tail))

    def _validate_schema_element_id(self, element_id):
        """
        Validate that each id of the elements is alphabetic.
        :param element_id: String.
        :return:
        """
        if not str.isalpha(element_id):
            raise ArgsException('Invalid schema format {}.'.format(element_id))

    def _parse_argument_list(self):
        """
        Parse the list of arguments passed to the class constructor.
        :return:
        """
        for argument in self._args:
            if argument.startswith('-'):
                try:
                    index_of = self._args.index(argument)
                    self._current_argument = self._args[index_of + 1]
                except IndexError:
                    pass
                finally:
                    self._set_marshaler_value(argument[1:])

    def _set_marshaler_value(self, argument_characters):
        """
        Update the marshaler value for the characters present in the map.
        :param argument_characters:
        :return:
        """
        marshaler = self._arguments.get(argument_characters)
        if marshaler:
            marshaler.set(self._current_argument)
        else:
            raise ArgsException('Invalid argument {}.'.format(
                argument_characters))

    def get_boolean_value(self, arg):
        """
        Retrieve the boolean value of an element according to its letter.
        :param arg: String
        :return:
        """
        return BooleanMarshaler.get_value(self._arguments.get(arg))

    def get_integer_value(self, arg):
        """
        Retrieve the integer value of an element according to its letter.
        :param arg: String
        :return:
        """
        return IntegerMarshaler.get_value(self._arguments.get(arg))

    def get_string_value(self, arg):
        """
        Retrieve the string value of an element according to its letter.
        :param arg: String
        :return:
        """
        return StringMarshaler.get_value(self._arguments.get(arg))

    def get_double_value(self, arg):
        """
        Retrieve the double value of the argument marshaler according to its
        letter.
        :param arg: String
        :return:
        """
        return DoubleMarshaler.get_value(self._arguments.get(arg))
