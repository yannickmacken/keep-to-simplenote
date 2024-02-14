This script converts exported notes from Google Keep to a notes.json file that can be imported by Simplenote.
Google Keep titles will be added as the first line in the content of the Simplenote note. 
Google Keep labels are converted in Simplenote tags.

# usage
* To export Google Keep notes as Json, see: https://takeout.google.com/.
Download the archive and extract the files. 
* This script is tested with python3.8. 
* Edit line 7 in the `convert.py` file, enter the absolute location of the folder with the Google Keep Json files. 
* From this folder, run ```python convert.py``` in your terminal.
* To import Json notes to Simplenote, open the desktop application at https://app.simplenote.com/ -> file -> import -> drag and drop.

# notes
* This version only converts Keep notes that are not Archived (see `convert.py` line 22).
You can modify this line, as required. 
* This version only converts Keep notes that include a `textContent` element (see `convert.py` line 22).
