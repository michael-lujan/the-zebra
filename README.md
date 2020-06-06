# The Zebra Take Home Assignment

# Assignment Walkthrough
objective:
    Parse CSV files, apply schema, and combine in the one CSV file
    Instructions in the "Instructions.pdf"

installation:
    clone repo
    open up a terminal
    change directory to the "the-zebra" directory
    run the following command in your terminal: pip install -U pytest

test:
    run the following command in your terminal: python3 -m pytest

setup:
    place any files you want to be combined in the "input" directory

run:
    run the following command in your terminal: python3 parse_and_combine_csvs.py
    
    The files in the "input" directory will be read. The "insurance" schema in the
    "schema" directory will be applied to the csv. And the transformed data will be
    written out into a single csv in the directory "output." 

# Thoughts
The solution works to combine files into one single csv. The app could be expanded in many ways. We can add a configuration file (input files, output path, schema, etc.), to read different formats from different sources, to write in different formats to different sources. If files become too large, the code can be adapted to read one unit (1 line, 50 lines, etc.) from the csv, apply schema, and place in output file in one unit of code, then process the next unit. If we want this to be faster, we can apply multiprocessing to process different files at the same time. If functional programming is the preference, much of the code can be reused to facilitate that kind of style.

