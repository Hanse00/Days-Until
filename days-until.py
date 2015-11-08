import datetime

a = datetime.date.today()
entry = raw_input("Enter date in format YYYY-MM-DD: ")

b = datetime.datetime.strptime(entry, "%Y-%m-%d").date()

d = b - a

if d.days <= 0:
    print "b must be later than a!"
elif d.days == 1:
    print "1 day"
else:
    print "{} days".format(d.days)
