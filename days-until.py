import datetime

print "Hello World!"

a = datetime.date(2015, 11, 8)
b = datetime.date(2015, 11, 9)

d = b - a

if d.days <= 0:
    print "b must be later than a!"
elif d.days == 1:
    print "1 day"
else:
    print "{} days".format(d.days)
