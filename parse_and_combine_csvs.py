import os
from zebra.csv_with_schema_combiner import CsvWithSchemaCombiner

def main():
    input_dir = 'input'
    output_dir = 'output'
    input_paths = [os.path.join(input_dir, file) \
        for file in os.listdir(input_dir) if file.endswith('.csv')]
    output_path = os.path.join(output_dir, 'result.csv')
    schema_path = os.path.join('schemas', 'insurance.csv')

    CsvWithSchemaCombiner(input_paths, schema_path, output_path) \
        .apply_schema_and_combine_csvs()

if __name__ == '__main__':
    main()