#!/usr/bin/python

from __future__ import print_function

from icalendar import Calendar
import sys

def get_key_value(a):
    val = ""
    if a.has_key("UID"):
        val = a["UID"]
    elif a.has_key("DTSTART"):
        val = a["DTSTART"]
    elif a.has_key("DESCRIPTION"):
        val = a["DESCRIPTION"]
    elif a.has_key("SUMMARY"):
        val = a["SUMMARY"]
    elif a.has_key("SUMMARY"):
        val = a["SUMMARY"]

    return val

if len(sys.argv) < 3:
    print("Usage: sort_ics.py in.ics out.ics")
    sys.exit(1)

cal = Calendar.from_ical(open(sys.argv[1], 'rb').read())

cal.subcomponents.sort(key=get_key_value)

# comps = cal.subcomponents
# print(comps)
# comps.sort(key=get_key_value)
# print(comps)

f = open(sys.argv[2], 'wb')
f.write(cal.to_ical())
f.close()
