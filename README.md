This script converts exported notes from Google Keep to a notes.json file that can be imported by SimpleNote.
Google Keep titles will be added as the first line in the content of the Simplenote note. 
Google Keep labels are converted in Simplenote tags.

# usage
To export Google Keep notes as Json, see: https://takeout.google.com/.
To import Simplenote notes as Json, open the desktop application -> file -> import -> drag and drop.
This script is tested with python3.8. 
In the convert.py file, enter the absolute location with Google Keep Json files. 
From this folder, run ```python convert.py``` in your terminal.
