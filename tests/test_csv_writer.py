import os
from zebra.csv_writer import *


def test_write_records_to_csv_with_header():
    records = [
        {'test 1': 'hi', 'test-2': 'red', 'test_3': 3.0, 'test4': 4.0},
        {'test 1': None, 'test-2': 'red', 'test_3': 3.0, 'test4': 4.0},
        {'test 1': 'hi', 'test-2': 'red', 'test_3': None, 'test4': 4.0}]

    test_path = 'test_write.csv'
    write_records_to_csv_with_header(records, test_path)
    expected = [
        'test 1,test-2,test_3,test4',
        'hi,red,3.0,4.0',
        ',red,3.0,4.0',
        'hi,red,,4.0']

    actual = None
    with open(test_path) as file:
        actual = [line.rstrip() for line in file]
    os.remove(test_path)
    assert len(expected) == len(actual)
    for e, a in zip(expected, actual):
        assert e == a


