#!/usr/bin/python
"""Report on differences between:
 BMCC*roster.csv - Roster spread sheet
 contraburners*.csv - Camp mailing list
"""

import csv

invited = "0123"

def ok(dgs):
  if not dgs:
    return False
  digit = dgs[0]
  return (digit in invited)

def main():
  verbose = True

  # read the camp roster and canonicalize it
  f = open("roster.csv", 'r')
#  f.readline() # discard comment about tickets
  roster = csv.DictReader(f)
  rows=[]
  rosteraddrs = {}
  for r in roster:
    if not r['Name']:
      continue
    rows.append(r)
    rosteraddrs[r['Preferred email address'].lower()] = r['Ticket status']
    rosteraddrs[r['Google email address'].lower()] = r['Ticket status']


  # read to googlegroup members
  f = open("contraburners2017.csv", 'r')
  f.readline() # discard the title
  email = csv.DictReader(f)


  listaddrs = {}
  print "Google group members registration statuses:"
  for l in email:
    a = l['Email address'].lower()
    listaddrs[a] = True
    if a not in rosteraddrs:
      print "Not registered:  %s <%s>,"%(l['Nickname'], a)
    elif not ok(rosteraddrs[a]):
      print "Extra:           %s <%s>,"%(l['Nickname'], a)
    elif verbose:
      print "Present:         %s <%s>,"%(l['Nickname'], a)

  print "Missing from Google group"
  for r in rows:
    if not ok(r['Ticket status']):
      continue
    a1 = r['Preferred email address'].lower()
    a2 = r['Google email address'].lower()
    if (a1 not in listaddrs) and (a2 not in listaddrs):
      if a2:
        print "  %s <%s>,"%(r['Name'], a2)
      if a1:
        print "  %s <%s>,"%(r['Name'], a1)

if __name__ == "__main__":
  main()
