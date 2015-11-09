import argparse
import datetime
import sys

class TimeContinuityError(ValueError):
    def __init__(self, date):
        self.value = "'{}' is not in the future!".format(date)

    def __str__(self):
        return repr(self.value)

def iso_date(string):
    try:
        date = datetime.datetime.strptime(string, "%Y-%m-%d").date()
        return date
    except ValueError:
        msg = "'{}' is not an ISO 8601 formatted date".format(string)
        raise argparse.ArgumentTypeError(msg)

def _parse_arguments(args):
    program_desc = ("a tool for calculating the number of days " +
        "(starting today) until a given date")
    date_arg_desc = ("the destination date, formatted as a zero padded ISO " +
        "8601 date string, Eg. 2015-11-08")
    human_arg_desc = ("human readable format, appends the word day or days " +
        "to the output as appropriate")
    help_arg_desc = "show this help message and exit"

    parser = argparse.ArgumentParser(description=program_desc, add_help=False)
    parser.add_argument("date", type=iso_date, help=date_arg_desc)
    parser.add_argument("-h", action="store_true", help=human_arg_desc)
    parser.add_argument("--help", action="help", help=help_arg_desc)
    return vars(parser.parse_args(args))

def _in_the_future(date):
    today = datetime.date.today()
    delta = (date - today).days

    return (delta > 0)

def _human_readable(delta):
    if delta == 1:
        return "1 day"
    else:
        return "{} days".format(delta)

def main(args):
    parsed_args = _parse_arguments(args)

    given_date = parsed_args["date"]
    human_readable_format = parsed_args["h"]

    if not _in_the_future(given_date):
        raise TimeContinuityError(given_date)

    today = datetime.date.today()
    delta = (given_date - today).days

    if human_readable_format:
        print _human_readable(delta)
    else:
        print delta

if __name__ == "__main__":
    main(sys.argv[1:])
