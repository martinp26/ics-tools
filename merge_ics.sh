#!/bin/sh
ec=1
now=`date -u +'%Y%m%dT%H%M%SZ'`

tfile1="/tmp/__sort_ics_tmp_file1-`basename \"$1\"`"
tfile2="/tmp/__sort_ics_tmp_file2-`basename \"$2\"`"

ifile1="/tmp/__sort_ics_in_file1-`basename \"$1\"`"
ifile2="/tmp/__sort_ics_in_file2-`basename \"$2\"`"

# filter away some often-conflicting lines and some ICS-standard violating lines
cat "$1" | sed -e "s/DTSTART:-4713010T000000/DTSTART:19000101T000000/g" | sed -e "s/DTSTART:1601/DTSTART:1900/g" | sed -e"s/DTSTART;VALUE=DATE:-4713010/DTSTART;VALUE=DATE:19000101/g" > "$ifile1"
cat "$2" | sed -e "s/DTSTART:-4713010T000000/DTSTART:19000101T000000/g" | sed -e "s/DTSTART:1601/DTSTART:1900/g" | sed -e"s/DTSTART;VALUE=DATE:-4713010/DTSTART;VALUE=DATE:19000101/g" > "$ifile2"

# create new container timestamps for $now and presort files
sort_ics.py "$ifile1" /dev/stdout | sed -e "s/^DTSTAMP.*$/DTSTAMP:"$now"/" > "$tfile1"
sort_ics.py "$ifile2" /dev/stdout | sed -e "s/^DTSTAMP.*$/DTSTAMP:"$now"/" > "$tfile2"

kdiff3  "$tfile1" "$tfile2" -o "$3"
ec=$?

rm "$tfile1" "$tfile2" "$ifile1" "$ifile2"
exit $ec
