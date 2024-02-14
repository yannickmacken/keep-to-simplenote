import json
from os import listdir
from os.path import isfile, join
from os import getcwd

# Path to Google Keep Json files (to export Google Keep notes as Json, see: https://takeout.google.com/)
folder_path = "C:/.../"

# Find filenames with Json extension
json_files_in_folder = [f for f in listdir(folder_path) if isfile(join(folder_path, f)) and ".json" in f]

# Initialize empty dict according to SimpleNotes import format
aggregate_dic = {
    "activeNotes": [],
    "trashedNotes": []
}

# Get content from all Google Keep Json files
for filename in json_files_in_folder:
    with open(join(folder_path, filename), encoding="utf-8") as f:
        dic = json.loads(f.read())
        if not dic['isArchived'] and 'textContent' in dic:
            aggregate_dic["activeNotes"].append(
                {
                    "content": dic["title"] + "\r\n\r\n" + dic["textContent"],
                    "tags": [label["name"] for label in dic.get("labels") or []]
                }
            )

# Write all content into SimpleNotes Json import file
with open(join(getcwd(), 'notes.json'), 'w') as f:
    f.write(json.dumps(aggregate_dic))

# To import, in SimpleNotes desktop app, open -> file -> import
