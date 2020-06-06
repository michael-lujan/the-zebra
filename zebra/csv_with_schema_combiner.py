import zebra.schema as schema
import zebra.parse_csv_with_schema as parser
import zebra.csv_writer as csv_writer
from functools import partial

class CsvWithSchemaCombiner:
    """
    A class used to take multiple csvs, apply a schema to them,
    and write out as one file.

    Attributes
    ----------
    input_paths : [str]
        list of strings of the paths of input csvs
    schema_path : str
        str of the path to the schema csv
    output_path : str
        str of the path to write out the combined csvs
    """
    def __init__(self, input_paths, schema_path, output_path):
        self.input_paths = input_paths
        self.schema_path = schema_path
        self.output_path = output_path

    def apply_schema_and_combine_csvs(self):
        expected_schema = schema.load_schema_from_csv(self.schema_path)

        records = []
        for path in self.input_paths:
            records += parser.parse_csv_records_accepted_by_schema(expected_schema, path)

        csv_writer.write_records_to_csv_with_header(records, self.output_path)
