#!/usr/bin/python3
"""script that adds arguments to a list
and loads to a json file."""

import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = "add_item.json"
try:
    obj = load_from_json_file(filename)
except Exception:
    obj = []

if __name__ == "__main__":
    """checks if the file is run
    at the command line as main."""
    if len(sys.argv) > 1:
        for i in sys.argv[1:]:
            obj.append(i)
    save_to_json_file(obj, filename)
