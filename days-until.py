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

def _parse_arguments(args):
    program_desc = ("a tool for calculating the number of days " +
        "(starting today) until a given date")
    date_arg_desc = ("the destination date, formatted as a zero padded ISO " +
        "date string, Eg. 2015-11-08")
    human_arg_desc = ("human readable format, appends the word day or days to" +
        "the output as appropriate")
    help_arg_desc = "show this help message and exit"

    parser = argparse.ArgumentParser(description=program_desc, add_help=False)
    parser.add_argument("date", type=iso_date, help=date_arg_desc)
    parser.add_argument("-h", action="store_true", help=human_arg_desc)
    parser.add_argument("--help", action="help", help=help_arg_desc)
    return vars(parser.parse_args(args))

def main(args):
    start = datetime.date.today()
    parsed_args = _parse_arguments(args)

    delta = parsed_args["date"] - start

    if delta.days <= 0:
        print "b must be later than a!"
    elif delta.days == 1:
        print "1 day"
    else:
        print "{} days".format(delta.days)

if __name__ == "__main__":
    main(sys.argv[1:])
