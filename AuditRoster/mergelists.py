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
  verbose = False

  # read the camp roster and canonicalize it (no output)
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

  # read to googlegroup members (no output)
  f = open("contraburners2021.csv", 'r')
  f.readline() # discard the title
  ggroup = csv.DictReader(f)
  listaddrs = {}
  for l in ggroup:
    a = l['Email address'].lower()
    listaddrs[a] = l['Nickname']

  # Generate a gmail pattern match
  pattern="( contraburner-board@googlegroups.com OR contraburner-organizers@googlegroups.com " +\
      "OR contraburners2021@googlegroups.com OR burningman.org or contraburners.org"
  stoplist={"matt.mathis@gmail.com", "mattmathis@gmail.com"}
  sep = ' OR '
  for addr in rosteraddrs:
    if addr not in stoplist:
      pattern += sep + addr
  pattern += ' )'
  print 'Gmail match: '+pattern

  print "\nGoogle group members who are registered as not participating"
  for a, nick in listaddrs.items():
    if a in rosteraddrs and not ok(rosteraddrs[a]):
      print "Extra:           %s <%s> (code:%s)"%(nick, a, rosteraddrs[a])

  print "\nGoogle group members who are properly registered"
  people, emails = 0,0
  for a, nick in listaddrs.items():
    if a in rosteraddrs and ok(rosteraddrs[a]):
      people += 1
      emails += addrcounts[a]
      if verbose:
        print "Present (%d):         %s <%s>,"%(addrcounts[a], nick, a)
  print "(%d people having %d total email addresses)"%(people,emails)

  print "\nGoogle group members who are not registered"
  for a, nick in listaddrs.items():
    if a not in rosteraddrs:
      print "%s <%s>,"%(nick, a)

  print "\nRegistered email but missing from Google group"
  for r in rows:
    if not ok(r['Ticket status']):
      continue
    a1 = r['Preferred email address'].lower()
    a2 = r['Google email address'].lower()
    if a1 and (a1 not in listaddrs):
      print "  %s <%s>,"%(r['Name'], a1)
    if a2 and (a1 != a2) and (a2 not in listaddrs):
      print "  %s <%s>,"%(r['Name'], a2)

if __name__ == "__main__":
  main()
