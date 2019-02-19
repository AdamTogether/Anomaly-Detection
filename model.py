#!/usr/bin/env python3

import sys
from clean import clean
from exp import explore


def model(dataset_filename):
    # Run the exploratory data analysis.
    explore(dataset_filename)

    # Get list of anomalies from clean function.
    anomaly_list = clean(dataset_filename)

    # Create "results.csv"
    with open("results.csv", "w+") as results:
        results.write(str("Anomaly Start Sample, Anomaly End Sample\n"))

        anomaly_start_position = None
        anomaly_end_position = None
        for current_row in anomaly_list:
            # If anomaly start and end positions are empty, set them both equal to the current row.
            if anomaly_start_position is None:
                anomaly_start_position = int(current_row)
                anomaly_end_position = int(current_row)

            # If current_row is a continuation of the anomaly, update end position with current_row.
            elif anomaly_end_position == current_row-1:
                anomaly_end_position = int(current_row)

            # If current_row is NOT a continuation of the anomaly, update start and end positions with current_row.
            elif anomaly_end_position < current_row-1:
                # Add current start and end positions to "results.csv".
                results.write(str(anomaly_start_position) + ", " + str(anomaly_end_position) + "\n")
                anomaly_start_position = int(current_row)
                anomaly_end_position = int(current_row)

            # If duplicate entry, it's the last anomaly. Add to "results.csv".
            elif anomaly_end_position == current_row:
                results.write(str(anomaly_start_position) + ", " + str(anomaly_end_position) + "\n")

    return 0


def main():
    # If the user did not provide a filename as an argument, default to "dataset.csv".
    if len(sys.argv) == 1:
        print("No arguments provided, using \"dataset.csv\" as input file...")
        model("dataset.csv")

    # If the user provided a filename as an argument, use the provided filename.
    elif len(sys.argv) == 2:
        dataset_filename = str(sys.argv[1])
        print("Using \"" + dataset_filename + "\" as input file...")
        model(dataset_filename)

    # Otherwise, too many arguments were given.
    else:
        print("ERROR: Too many arguments provided.")
        print("Usage: ./model.py [DATASET_FILENAME]")

    exit(0)


if __name__ == '__main__':
    main()
