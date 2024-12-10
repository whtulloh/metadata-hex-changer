# PURPOSE
To change the Metadata that can be looked in using HEX editor.

Metadata:
- startdate: change to the current date from the template
- endate: change to the current date from the template

## Logic
- store metadata template in the config.ini file
- get current date and convert to HEX
- replace the metadata template with new HEX

## RUN
```main.py --templatenumber "33-1" --startdate "2024-09-03T12:00:00.000" --enddate "2024-09-03T12:02:00.000"```