
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from scripts.remove_duplicates import remove_duplicates

def test_duplicates_removed():

    input_file = "data/dataset.csv"
    output_file = "data/test_output.csv"

    remove_duplicates(input_file, output_file)

    df = pd.read_csv(output_file)

    assert df.duplicated().sum() == 0
