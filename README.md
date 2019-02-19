# Anomaly Detection

The Python scripts in this folder were created for ExtraHop's Data Science Coding Challenge for Anomaly Detection (Version 1.0).

## Installation

This project was written using [Python 3.6.7](https://www.python.org/downloads/release/python-367/) on [Ubuntu 16.04 (Xenial)](http://hr.releases.ubuntu.com/16.04.5/). The following instructions assume you are using a Linux workstation with Python 3.X.X.

First, if you don't already have pip installed:
```bash
sudo apt install python3-pip
```

Verify that [pip](https://pip.pypa.io/en/stable/) is version 10.0.1 or higher:
```bash
python3 -m pip --version
```

If not, upgrade pip:
```bash
python3 -m pip install --upgrade pip==10.0.1
```

Install the required dependencies:
```bash
sudo python3 -m pip install numpy
sudo python3 -m pip install pandas
sudo python3 -m pip install matplotlib
sudo apt-get install python3-tk
```

Navigate to this project's directory and ensure proper execution priveleges:
```bash
chmod +x *.py
```

Run dos2unix on the dataset and python scripts to guarantee that no invisible characters were added to the file during its migration:
```bash
sudo apt-get install dos2unix
dos2unix dataset.csv && dos2unix *.py
```

## Usage

To run the script on "dataset.csv" as given by the challenge, simply run:
```bash
./model.py
```
This will automatically run both the data exploration and data cleaning scripts. It will also generate a file called "cleaned_dataset.csv" within this folder.

---
To run the other scripts independently:
```bash
./exp.py	# This will execute the data exploration script on "dataset.csv".
./clean.py	# This will execute the data cleaning script on "dataset.csv".
```

To specify a different dataset:
```bash
./model.py [FILE]
./exp.py [FILE]
./clean.py [FILE]
```

## Author
Adam Stewart

## License
[MIT](https://choosealicense.com/licenses/mit/)
