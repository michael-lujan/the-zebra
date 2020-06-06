import pytest
from zebra.csv_reader import *

def test_read_csv_with_header(test_home_insurance_csv_file):
    path, lines = test_home_insurance_csv_file
    expected_column_names, records = read_csv_with_header(path)

    for index, line in enumerate(lines):
        if index == 0: # line is header
            actual_column_names = line.split(',')
            assert len(expected_column_names) == len(actual_column_names)
            for expected, actual in zip(expected_column_names, actual_column_names):
                assert expected == actual
        else: # check that records match csv content
            record = records[index-1]
            actual_values = line.split(',')
            for expected, (column_name, actual) in zip(actual_values, record.items()):
                #TODO: fix in later iteration if need be
                expected = expected.replace('"""', '"')
                assert expected == actual
