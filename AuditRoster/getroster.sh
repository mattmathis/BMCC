#! /bin/bash

roster="https://docs.google.com/spreadsheets/d/1h_dcOkk0xgs3XT0YqBieEPjJ0wYqXBOHXU76NV-pghs"
wget "$roster/export?format=csv" -O roster.csv
