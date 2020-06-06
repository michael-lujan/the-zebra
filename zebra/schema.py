import pandas

def load_schema_from_csv(path):
    '''loads schema from a csv file
    returns a list of column dicts with properties of the column
    '''
    schema_df = pandas.read_csv(path)
    schema = []
    for index, row in schema_df.iterrows():
        column = {}
        column['name'] = row['name']
        column['type'] = row.type
        column['is_nullable'] = True if row['is_nullable'].lower() == 'yes' else False
        column['version'] = str(row['version'])
        schema.append(column)
    return schema

def is_schema_within_columns(schema, columns):
    '''checks if all schema columns are included in columns
    '''
    expected_columns_set = set([column['name'] for column in schema])
    input_columns_set = set(columns)
    return len(expected_columns_set.intersection(input_columns_set)) == len(expected_columns_set)

def create_record_with_schema(schema, data):
    '''convert data into schema'd data
        returns dict with key-value pairings where key is column_name and value is the
        converted value to the schema data type
        errors if a schema column is not in data or a non-nullable column is null
    '''
    record = {}
    for column in schema:
        name = column['name']
        data_type = column['type']
        record[name] = _convert_to_type(data[name], data_type)
        if record[name] == None and not column['is_nullable']:
            raise Exception('Null value found for non-nullable column: {}'.format(name))
    return record

#TODO: check on quotes situation
def _convert_to_type(value, data_type):
    if type(value) == str and value == '':
        return None

    if data_type.lower() == 'string':
        if value == '':
            return None
        return str(value)
    elif data_type.lower() in ['float']:
        if type(value) == float:
            return value
        return float(value.replace('"', ''))
    elif data_type.lower() in ['int', 'integer']:
        if type(value) == int:
            return value
        return int(value.replace('"', ''))

    raise Exception('COULD NOT PARSE {} AS TYPE {}'.format(value, data_type)) 