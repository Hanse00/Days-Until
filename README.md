# Days Until

Days until is a small python utility, for calculating the number of days until a given date.

## Requirements
* Python 2.7

## Script
### Function

The script calculates the number of days between the current date (calculated as `datetime.date.today()`) and the date provided in the ISO 8601 format (YYYY-MM-DD).

The number of days between now and then, is defined as the number of 24 hour periods between the dates. Meaning it's not the actual days between the two days, inclusive or exclusively. For example the number of days between today, and tomorrow is 1.

The script takes a number of parameters, as detailed below.

### Usage
```
python days-until.py [-h] [--help] date
```
### Positional Arguments
Argument|Explenation
--------|-----------
date    |An ISO 8610 formatted date string

### Optional Arguments
Argument|Explenation|Default
--------|-----------
--help  |Print the help message and exit|False
-h      |Print the number of days in human readable format|False

### Example
```
python days-until.py 2015-11-10
> 1

python days-until.py 2015-11-10 -h
> 1 day
```

## License

The project is licensed under the MIT license, in brief it means you can do anything you want with the code.

Check [license][] for full license specifications.

[license]: LICENSE "Full License"
