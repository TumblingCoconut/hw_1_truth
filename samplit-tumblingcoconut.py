import pandas as pd
import argparse
import random

def main():
    parser = argparse.ArgumentParser(description="A CLI script for sampling a csv")
    parser.add_argument("csv_name", type=str, help="CSV file name")
    args = parser.parse_args()

    try:
        df = pd.read_csv(args.csv_name)
    except FileNotFoundError as e:
        print("File name not found")

    for _, row in df.iterrows():
        if random.random() < 0.01:
            print(list(row))

if __name__ == "__main__":
    main()
