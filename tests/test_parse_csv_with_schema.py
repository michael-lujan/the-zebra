import pytest
from zebra.parse_csv_with_schema import *

def test_parse_csv_with_matching_schema(test_schema, test_schema_match_csv_file, test_schema_match_records):
    path, lines = test_schema_match_csv_file
    expected = test_schema_match_records
    actual = parse_csv_records_accepted_by_schema(test_schema, path)
    _assert_dictionaries_matching(expected, actual)

def test_parse_csv_with_schema_included(test_schema, test_schema_included_csv_file, test_schema_included_records):
    path, lines = test_schema_included_csv_file
    expected = test_schema_included_records
    actual = parse_csv_records_accepted_by_schema(test_schema, path)
    _assert_dictionaries_matching(expected, actual)

def test_parse_csv_with_schema_mismatch(test_schema, test_schema_mismatch_csv_file, test_schema_mismatch_records):
    path, lines = test_schema_mismatch_csv_file
    expected = test_schema_mismatch_records
    actual = parse_csv_records_accepted_by_schema(test_schema, path)
    _assert_dictionaries_matching(expected, actual)

def _assert_dictionaries_matching(expected, actual):
    assert len(expected) == len(actual)
    for expected_column, actual_column in zip(expected, actual):
        for key, value in expected_column.items():
            assert value == actual_column[key]