# epadd_utils
Python scripts for manipulating ePADD output. Work in progress

## Getting Started

Install the package locally by cloning the repo

```
git clone https://github.com/AmericanPhilosophicalSociety/epadd_utils.git
cd epadd_utils
```

Alterntively, download the repo as a Zip file, unzip it, and navigate to the repo using your preferred terminal.

## Converting ePADD output to a CSV

Run the following command, specifying your desired input and output files:

```
python epadd_utils/parse-email-list.py /path/to/text/file.txt /destination/output.csv
```

## Converting a CSV to ePADD output

Run the following command, specifying your desired input and output files:

```
python epadd_utils/parse-csv.py /path/to/csv.csv /destination/output.txt
```

You can optionally specify a delimiter for subsections in the CSV, if needed (```|``` is default):

```
# use a semicolon as a delimiter
python epadd_utils/parse-csv.py --delimiter ";" /path/to/csv.csv /destination/output.txt
```