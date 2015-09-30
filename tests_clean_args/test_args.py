# -*- coding: utf-8 -*-
"""
Test suite for CleanArgs code Kata based on the Clean Code book by Uncle Bob.
"""
__author__ = 'cllamach'

from clean_args.args import CleanArgs
from clean_args.args_exception import ArgsException
import pytest


def test_args_get_boolean_value():
    args = CleanArgs('l', ['-l'])
    assert args.get_boolean_value('l')


def test_args_get_boolean_false_when_no_valid_schema():
    args = CleanArgs('l*', ['-l', '9000'])
    assert not args.get_boolean_value('l')


def test_schema_passed_is_not_valid():
    with pytest.raises(ArgsException) as e:
        CleanArgs('l$', ['-l', '190'])
    assert str(e.value) == '$ is not a valid schema value.'


def test_args_integer_return_value():
    args = CleanArgs('p*', ['-p', '99'])
    assert args.get_integer_value('p') == 99


def test_args_receive_invalid_integer():
    with pytest.raises(ArgsException) as e:
        CleanArgs('p*', ['-p', 'not_integer'])

    assert str(e.value) == 'Expected integer but got not_integer.'


def test_args_does_not_receive_argument():
    with pytest.raises(ArgsException) as e:
        CleanArgs('p*', ['-l'])

    assert str(e.value) == 'Invalid argument l.'


def test_passed_invalid_schema_character():
    with pytest.raises(ArgsException) as e:
        CleanArgs('2*', ['-2', '9989'])

    assert str(e.value) == 'Invalid schema format 2.'


def test_passed_invalid_schema_character_symbol():
    with pytest.raises(ArgsException) as e:
        CleanArgs('&*', ['-&', '1231'])

    assert str(e.value) == 'Invalid schema format &.'


def test_passed_arguments_returns_correct_values():
    args = CleanArgs('l,p*', ['-l', '-p', '99'])

    assert args.get_integer_value('p') == 99
    assert args.get_boolean_value('l')


def test_passed_arguments_returns_false_when_not_called():
    args = CleanArgs('l,p*', ['-p', '1900'])

    assert not args.get_boolean_value('l')
    assert args.get_integer_value('p') == 1900


def test_passed_arguments_without_mark():
    args = CleanArgs('l,p*', ['l', '-p', '9900'])

    assert not args.get_boolean_value('l')
    assert args.get_integer_value('p')


def test_string_argument_format():
    args = CleanArgs('s#', ['-s', '/home/cllamach'])

    assert args.get_string_value('s') == '/home/cllamach'


def test_string_argument_not_found():
    with pytest.raises(ArgsException) as e:
        args = CleanArgs('s#', ['-s'])
        args.get_string_value('s')

    assert str(e.value) == 'Expected string but found None.'


def test_double_argument_found():
    args = CleanArgs('d##', ['-d', '999.29'])

    assert args.get_double_value('d') == 999.29


def test_double_argument_invalid_double():
    with pytest.raises(ArgsException) as e:
        CleanArgs('d##', ['-d', 'InvalidDouble'])

    assert str(e.value) == 'Expected double value but got InvalidDouble.'


def test_double_parameter_missing():
    args = CleanArgs('d##,p*', ['-p', '990'])

    assert args.get_double_value('-d') == 0.0


def test_double_parameter_empty():
    with pytest.raises(ArgsException) as e:
        CleanArgs('d##', ['-d'])

    assert str(e.value) == 'Expected double value but got None.'


def test_string_list_parameter_found():
    args = CleanArgs('l[*]', ['-l', 'Hello World'])

    assert args.get_string_list_value('l') == ['Hello', 'World']

