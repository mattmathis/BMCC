#!/usr/bin/python
"""Report on differences between:
 BMCC*roster.csv - Roster spread sheet
 contraburners*.csv - Camp mailing list
"""

import csv
import collections

invited = "01234"

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
  addrcounts = collections.Counter()
  for r in roster:
    if not r['Name']:
      continue
    rows.append(r)
    for col in {'Preferred email address', 'Google email address'}:
      addr = r[col].lower()
      if addr == '':
        continue
      rosteraddrs[addr] = r['Ticket status']
      addrcounts[addr] += 1

  # read to googlegroup members
  f = open("contraburners2019.csv", 'r')
  f.readline() # discard the title
  email = csv.DictReader(f)

  # Generate a gmail pattern match
  pattern = ''
  sep = '( '
  for addr in rosteraddrs:
    pattern += sep + addr
    sep = ' OR '
  pattern += ' )'
  print 'Gmail match: '+pattern

  listaddrs = {}
  print "Google group member registration statuses:"
  for l in email:
    a = l['Email address'].lower()
    listaddrs[a] = True
    if a not in rosteraddrs:
      print "Not registered:  %s <%s>,"%(l['Nickname'], a)
    elif not ok(rosteraddrs[a]):
      print "Extra:           %s <%s> (code:%s)"%(l['Nickname'], a, rosteraddrs[a])
    elif verbose:
      print "Present (%d):         %s <%s>,"%(addrcounts[a], l['Nickname'], a)

  print "Missing from Google group"
  for r in rows:
    if not ok(r['Ticket status']):
      continue
    a1 = r['Preferred email address'].lower()
    a2 = r['Google email address'].lower()
    if (a1 not in listaddrs) and (a2 not in listaddrs):
      if a2:
        print "  %s <%s>,"%(r['Name'], a2)
      else:
        print "  %s <%s>,"%(r['Name'], a1)

if __name__ == "__main__":
  main()
