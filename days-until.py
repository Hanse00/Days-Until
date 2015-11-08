import argparse
import datetime

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

parser = argparse.ArgumentParser(description=program_desc)
parser.add_argument("date", type=iso_date, help=date_arg_desc)
print parser.parse_args("2015-12-24 -h".split())

#a = datetime.date.today()
#entry = raw_input("Enter date in format YYYY-MM-DD: ")

#b = datetime.datetime.strptime(entry, "%Y-%m-%d").date()

#d = b - a

#if d.days <= 0:
#    print "b must be later than a!"
#elif d.days == 1:
#    print "1 day"
#else:
#    print "{} days".format(d.days)
