# import pandas as pd

# file = "numplate.csv"
# df = pd.read_csv(file)
# pd.options.display.max_columns = len(df.columns)
# print(df)

import csv

def print_cols(data):
    col_spacer = "  "       # added between columns
    widths = [max(len(str(item)) for item in row) for row in zip(*data)]
    print('\n'.join(col_spacer.join(f"{col:{widths[index]}}" for index, col in enumerate(row)) for row in data))

with open("numplate.csv") as f1:
    csv_r = csv.reader(f1)
    data = list(csv_r)

print_cols(data)