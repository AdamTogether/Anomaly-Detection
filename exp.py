#!/usr/bin/env python3

import sys
import pandas
import matplotlib.pyplot as plt


def explore(dataset_filename):
    # Read dataset into dataframe.
    dataframe = pandas.read_csv(dataset_filename)

    # Create array of headers to reference each column of the dataset. 
    header_array = []
    for header in dataframe:
        header_array.append(header)

    # Print the dataframe to the terminal.
    print(dataframe)

    # Plot the imported dataset as it was given prior to cleaning.
    plt.plot(dataframe[header_array[1]], 'r', dataframe[header_array[2]], 'b')
    plt.title(str(dataset_filename))
    plt.xlabel('Sample #')
    plt.ylabel('Value')
    plt.show()

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
