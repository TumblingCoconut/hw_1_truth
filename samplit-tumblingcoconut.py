import pandas as pd
import argparse
import random

def main():
    # CLI parser for csv file name
    parser = argparse.ArgumentParser(description="A CLI script for sampling a csv")
    parser.add_argument("csv_name", type=str, help="CSV file name")
    args = parser.parse_args()
    
    # try/except for csv file name
    try:
        df = pd.read_csv(args.csv_name)
    except FileNotFoundError as e:
        print("File name not found")
    
    # iterate and sample csv
    for _, row in df.iterrows():
        if random.random() < 0.01:
            print(list(row))

if __name__ == "__main__":
    main()
