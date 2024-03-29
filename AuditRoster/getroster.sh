#! /bin/bash

# Exported googlegroup
mailinglist=contraburners2022.csv
listfile=$HOME/Downloads/$mailinglist

# Roster Google docs in successive years
roster17="https://docs.google.com/spreadsheets/d/1h_dcOkk0xgs3XT0YqBieEPjJ0wYqXBOHXU76NV-pghs"
roster18="https://docs.google.com/spreadsheets/d/1QaukY9NbAVqL5CKkOrDjGVKcS6D56lDWO_LmOkuXh98"
roster19="https://docs.google.com/spreadsheets/d/1tRnJuQ7-NdI_9wimOBFgRYFeL8akyfgf4YO4OnHHvBo"
roster20="https://docs.google.com/spreadsheets/d/1ylJqm0vBadCqNqCxZ2ew9BSZ8E_UYi12ewfdXBiZuvg"
roster21="https://docs.google.com/spreadsheets/d/1abmr0w6gLQMneMdWzXIgdv2bDW5DFTSUrV-CC8SUzsU"
roster22="https://docs.google.com/spreadsheets/d/1K8z7hpk0ZXSGP6lHdepIxO6Ax73byZYY5yW4ksm1IPs"

# echo "Fetch Roster" (must be "anybody with link")
wget "$roster22/export?format=csv" -O roster.csv

if [ -f $listfile ]; then
  echo "Updating mailing list"
  mv $listfile .
else
  echo "Keeping existing previously fetched mailing list rm $mailinglist"
fi

./mergelists.py
