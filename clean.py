#!/usr/bin/env python3

import sys
import pandas
import matplotlib.pyplot as plt


def clean(dataset_filename):
    # Suppress pandas' warnings for chained assignment.
    pandas.options.mode.chained_assignment = None  # default='warn'

    # Read dataset into dataframe.
    dataframe = pandas.read_csv(dataset_filename)

    # Create array of headers to reference each column of the dataset. 
    header_array = []
    for header in dataframe:
        header_array.append(header)

    # Create list to record anomalies.
    anomaly_list = []

    # Iterate through each row and check for anomalies.
    for i in range(0, len(dataframe[header_array[0]])):
        # If a sensor value is empty, add it to the anomaly list.
        if str(dataframe[header_array[1]][i]) == 'nan' or str(dataframe[header_array[2]][i]) == 'nan':
            # If 'Sensor 1' is empty, add it to the anomaly list.
            if str(dataframe[header_array[1]][i]) == 'nan':
                anomaly_list.append(dataframe[header_array[0]][i])
            # Otherwise 'Sensor 2' is empty, add it to the anomaly list.
            else:
                anomaly_list.append(dataframe[header_array[0]][i])

        # If current value varies significantly more than the preceding two values, set equal to 'None'.
        else:
            if i > 1:
                # Calculate the difference of the current row and previous row for 'Sensor 1'.
                current_difference_1 = abs(dataframe[header_array[1]][i]-dataframe[header_array[1]][i-1])
                previous_difference_1 = abs(dataframe[header_array[1]][i-1]-dataframe[header_array[1]][i-2])

                # Check the value for 'Sensor 1'.
                if current_difference_1 > 3*previous_difference_1:
                    # Add the value to the anomaly list.
                    anomaly_list.append(dataframe[header_array[0]][i])

                    # Delete the datum to allow the value to be filled in using linear interpolation.
                    dataframe[header_array[1]][i] = None

                # Calculate the difference of the current row and previous row for 'Sensor 2'.
                current_difference_2 = abs(dataframe[header_array[2]][i]-dataframe[header_array[2]][i-1])
                previous_difference_2 = abs(dataframe[header_array[2]][i-1]-dataframe[header_array[2]][i-2])

                # Check the value for 'Sensor 2'.
                if current_difference_2 > 3*previous_difference_2:
                    # Add the value to the anomaly list.
                    anomaly_list.append(dataframe[header_array[0]][i])

                    # Delete the datum to allow the value to be filled in using linear interpolation.
                    dataframe[header_array[2]][i] = None

    # Convert dataframe's indices to datetime in nanoseconds to allow for linear interpolation.
    dataframe[header_array[1]].index = pandas.to_datetime(dataframe[header_array[1]].index, unit='ns')
    dataframe[header_array[2]].index = pandas.to_datetime(dataframe[header_array[2]].index, unit='ns')

    # Resample dataframe using linear interpolation, store as a new series.
    interpolated_sensor1 = (dataframe[header_array[1]].resample('ns').mean().interpolate('linear'))
    interpolated_sensor2 = (dataframe[header_array[2]].resample('ns').mean().interpolate('linear'))

    # Convert dataframe's indices back to numeric values to plot the dataset with correct sample numbers.
    interpolated_sensor1.index = pandas.to_numeric(interpolated_sensor1.index)
    interpolated_sensor2.index = pandas.to_numeric(interpolated_sensor2.index)

    # Create "clean_dataset.csv".
    with open("clean_dataset.csv", "w+") as clean_dataset:
        # Write headers to csv (spaces are included in header_array).
        clean_dataset.write(str(header_array[0]) + "," + str(header_array[1]) + "," + str(header_array[2]) + "\n")

        # Write the sample # and both sensor values to "clean_dataset.csv".
        for i in range(0, len(interpolated_sensor1)):
            clean_dataset.write(str(i) + "," + str(interpolated_sensor1[i]) + "," + str(interpolated_sensor2[i]) + "\n")

    # Now that anomalies are recorded, and the dataset is cleaned, plot the cleaned dataset.
    plt.plot(interpolated_sensor1, 'r', interpolated_sensor2, 'b')
    plt.title('clean_dataset.csv')
    plt.xlabel('Sample #')
    plt.ylabel('Value')
    plt.show()

    return anomaly_list


def pretty_print(row, sensor1, sensor2):
    if len(str(sensor1)) >= 16:
        print(str(row) + "\t" + str(sensor1) + "\t" + str(sensor2))
    elif len(str(sensor1)) >= 12:
        print(str(row) + "\t" + str(sensor1) + "\t\t" + str(sensor2))
    else:
        print(str(row) + "\t" + str(sensor1) + "\t\t\t" + str(sensor2))


def main():
    # If the user did not provide a filename as an argument, default to "dataset.csv".
    if len(sys.argv) == 1:
        print("No arguments provided, using \"dataset.csv\" as input file...")
        clean("dataset.csv")

    # If the user provided a filename as an argument, use the provided filename.
    elif len(sys.argv) == 2:
        dataset_filename = str(sys.argv[1])
        print("Using \"" + dataset_filename + "\" as input file...")
        clean(dataset_filename)

    # Otherwise, too many arguments were given.
    else:
        print("ERROR: Too many arguments provided.")
        print("Usage: ./clean.py [DATASET_FILENAME]")

    exit(0)


if __name__ == "__main__":
    main()
