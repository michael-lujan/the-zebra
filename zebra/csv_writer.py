import pandas

def write_records_to_csv_with_header(records, path):
    dataframe = pandas.DataFrame(records)
    pandas.set_option('max_columns', None)
    print(dataframe)
    dataframe.to_csv(path, index=False)



