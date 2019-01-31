#!/usr/bin/env python3

import sys


def explore(p_dataset):
    return 0


def main():
    # If the user did not provide a filename as an argument, default to "dataset.csv".
    if len(sys.argv) == 1:
        print("No arguments provided, using \"dataset.csv\" as input file...")
        explore("dataset.csv")
    # If the user provided a filename as an argument, use the provided filename.
    elif len(sys.argv) == 2:
        dataset_filename = str(sys.argv[1])
        print("Using \"" + dataset_filename + "\" as input file...")
        explore(dataset_filename)
    # Otherwise, too many arguments were given.
    else:
        print("ERROR: Too many arguments provided.")
        print("Usage: ./exp.py [DATASET_FILENAME]")
    exit(0)


if __name__ == "__main__":
    main()
