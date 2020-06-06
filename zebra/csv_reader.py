import csv

def read_csv_with_header(path):
    '''reads a csv that has a header (first row is the column names)
    returns (columns, records)
        columns: list of column names from the header of the csv
        records: list of dicts where each dict is a key-value pairing of column name and value
    '''
    records = []
    with open(path, 'r') as file:
        reader = csv.DictReader(file, delimiter=',')
        for record in reader:
            records.append(record)
    return reader.fieldnames, records