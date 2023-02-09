#!/usr/bin/python3
"""Report on differences between:
 BMCC*roster.csv - Roster spread sheet
 contraburners*.csv - Camp mailing list
"""

import csv
import collections

def readRoster(addrs, fname, skip=0):
  f = open(fname, 'r')
  for i in range(skip):
    f.readline() # discard garbage at the top
  roster = csv.DictReader(f)
  rows=[]
  for r in roster:
    if not r['Name']:
      continue
    rows.append(r)
    for col in {'Preferred email address', 'Google email address'}:
      addr = r[col].lower()
      if addr == '':
        continue
      addrs[addr] = r['Ticket status']
  return(rows)

def readGroup(listaddrs, fname):
  f = open(fname, 'r')
  f.readline() # discard the title
  ggroup = csv.DictReader(f)
  for l in ggroup:
    a = l['Email address'].lower()
    listaddrs[a] = l['Nickname']

# Check for people marked not to be invited
invited = "01234"
def ok(dgs):
  return(dgs != "Xreg-no")

def main():
  verbose = False

  # read the camp roster and canonicalize it (no output)
  rosteraddrs = {}
  rows=readRoster(rosteraddrs, "roster19.csv")

  # read to googlegroup members (no output)
  listaddrs = {}
  readGroup(listaddrs, "contraburners2019.csv")

  print ("\nGoogle group members who are registered as not participating")
  for a, nick in listaddrs.items():
    if a in rosteraddrs and not ok(rosteraddrs[a]):
      print ("Extra:           %s <%s> (code:%s)"%(nick, a, rosteraddrs[a]))


  print ("\nGoogle group members who are not registered")
  for a, nick in listaddrs.items():
    if a not in rosteraddrs:
      print ("%s <%s>,"%(nick, a))

  print ("\nRegistered email but missing from Google group")
  for r in rows:
    if not ok(r['Ticket status']):
      continue
    a1 = r['Preferred email address'].lower()
    a2 = r['Google email address'].lower()
    if a1 and (a1 not in listaddrs) and (a2 not in listaddrs):
      print ("  %s <%s>,"%(r['Name'], a1))
if __name__ == "__main__":
  main()
