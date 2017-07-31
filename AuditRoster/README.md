# Audit Roster

Scripts to fetch and compare the main camp roster against the main Google group.

## Instructions

- Visit the contraburners2017 googlegroup  management page: https://groups.google.com/forum/#!managemembers/contraburners2017/members/active 
- Click "export members" and save the CSV file someplace convenient.
- In the same location run getroster.sh to fetch the camp roster.
- Run mergelists.py to produce a report

The first pass scans through the Google group and reports if the email addresses are present in the roster.  "Present and "Not Registered" are self explanatory.  "Extra" means that they are registered but their status indicates that they are not camping with us.  This is usually OK.

(Note that since many people have multiple email addresses, there can be false "Not registered" statuses).

The second pass scans through the roster and confirms that at least one email address for each person is present in the Google group.  Again some people use different addresses for the Google group and their registration.
