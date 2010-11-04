#!/usr/bin/python

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

def uid_sort(a, b):
    # fixme: we could protect us here against (invalid) UID-less components
    a_val = get_key_value(a)
    b_val = get_key_value(b)

    if a_val > b_val:
        return 1
    elif a_val < b_val:
        return -1
    else:
        return 0

if len(sys.argv) < 3:
    print "Usage: sort_ics.py in.ics out.ics"
    sys.exit(1)

cal = Calendar.from_string(open(sys.argv[1], 'rb').read())

cal.subcomponents.sort(uid_sort)

# print comps
# comps.sort(uid_sort)
# print comps

f = open(sys.argv[2], 'wb')
f.write(cal.as_string())
f.close()
