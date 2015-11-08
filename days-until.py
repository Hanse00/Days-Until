import argparse
import datetime
import sys

def iso_date(string):
    try:
        date = datetime.datetime.strptime(string, "%Y-%m-%d").date()
        return date
    except ValueError:
        msg = "'{}' is not an ISO formatted date".format(string)
        raise argparse.ArgumentTypeError(msg)

program_desc = ("A tool for calculating the number of days (Starting today) " +
    "until a given date.")
date_arg_desc = ("The destination date, formatted as a zero padded ISO date" +
    "string. Eg. 2015-11-08")

def main(args):
    a = datetime.date.today()

    parser = argparse.ArgumentParser(description=program_desc)
    parser.add_argument("date", type=iso_date, help=date_arg_desc)
    b = vars(parser.parse_args(args))["date"]

    delta = b - a

    if delta.days <= 0:
        print "b must be later than a!"
    elif delta.days == 1:
        print "1 day"
    else:
        print "{} days".format(delta.days)

if __name__ == "__main__":
    main(sys.argv[1:])
