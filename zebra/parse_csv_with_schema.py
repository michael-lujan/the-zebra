import csv
from zebra.schema import *
from zebra.csv_reader import *

def parse_csv_records_accepted_by_schema(schema, path):
    ''' parses csv and applies schema to records
        returns (processed_records, unprocessed_records)
        processed_records: a list of dicts with key-value pairings where key is column_name and value is the
        converted value to the schema data type.
        records not included if a schema column is not in data or a non-nullable column is null
    '''
    columns, unprocessed_records = read_csv_with_header(path)
    processed_records = []
    if is_schema_within_columns(schema, columns):
        for unprocessed_record in unprocessed_records:
            try:
                record = create_record_with_schema(schema, unprocessed_record)
                processed_records.append(record)
            except Exception as e:
                print('Warning: record not processed\nrecord: {}\nMessage: {}'.format(
                    unprocessed_record, e))
    return processed_records

