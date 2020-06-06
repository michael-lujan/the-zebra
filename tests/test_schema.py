import pytest
from zebra.schema import *
from zebra.schema import _convert_to_type

def test_load_schema_from_csv(test_schema_csv_file, test_schema):
    test_schema_path, lines = test_schema_csv_file
    expected = test_schema
    actual = load_schema_from_csv(test_schema_path)
    _assert_dictionaries_matching(expected, actual)

def _assert_dictionaries_matching(expected, actual):
    assert len(expected) == len(actual)
    for expected_column, actual_column in zip(expected, actual):
        for key, value in expected_column.items():
            assert value == actual_column[key]

def test_schema_is_within_columns():
    empty_schema = []
    
    # empty schema and empty columns
    expected = True
    columns = []
    actual = is_schema_within_columns(empty_schema, columns)
    assert expected == actual

    # empty schema and non-empty columns
    expected = True
    columns = ['test1']
    actual = is_schema_within_columns(empty_schema, columns)
    assert expected == actual

    test_schema = [
        {'name': 'test 1', 'type': 'String', 'is_nullable': True, 'version': '1'},
        {'name': 'test2', 'type': 'String', 'is_nullable': True, 'version': '1'}]

    # test schema columns and columns are same
    expected = True
    columns = ['test 1', 'test2']
    actual = is_schema_within_columns(test_schema, columns)
    assert expected == actual

    # columns have test schema columns and more
    expected = True
    columns = ['test 1', 'test2', 'test_3']
    actual = is_schema_within_columns(test_schema, columns)
    assert expected == actual
    
    # test schema columns and columns have nothing in common
    expected = False
    columns = ['test 4', 'test3']
    actual = is_schema_within_columns(test_schema, columns)
    assert expected == actual
    
    # columns has some of test schema columns but not all
    expected = False
    columns = ['test 1']
    actual = is_schema_within_columns(test_schema, columns)
    assert expected == actual

    # test schema columns and empty columns
    expected = False
    columns = []
    actual = is_schema_within_columns(test_schema, columns)
    assert expected == actual

def test_create_record_with_schema(test_schema, test_home_insurance_csv_file):
    expected = {'test 1': 'test1', 'test-2': 'test2', 'test_3': 3.0, 'test4': 4.0}
    record = {'test 1': 'test1', 'test-2': 'test2', 'test_3': '3', 'test4': '4'}
    actual = create_record_with_schema(test_schema, record)
    assert len(expected.items()) == len(actual.items())
    for column in test_schema:
        assert type(expected[column['name']]) == type(actual[column['name']])
        assert expected[column['name']] == actual[column['name']]

def test_convert_to_type_unknown_type():
    data_type = '¯|_(ツ)_|¯'

    value = 'test'
    try:
        _convert_to_type(value, data_type)
        assert False
    except:
        pass

def test_convert_to_type_string():
    data_type = 'string'

    value = 1
    expected = '1'
    actual = _convert_to_type(value, data_type)
    assert expected == actual

    value = None
    expected = 'None'
    actual = _convert_to_type(value, data_type)
    print(actual)
    assert expected == actual
