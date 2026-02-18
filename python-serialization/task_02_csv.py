#!/usr/bin/python3

"""CSV -> JSON"""
import csv
import json


def convert_csv_to_json(filename):
    """read things in the csv and convert to json"""
    #  Read CSV
    try:
        with open(filename, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            #  List of dictionaries
            data = [row for row in reader]

        #  Convert to dictionary and JSON
        json_data = json.dumps(data, indent=4)
        with open("data.json", "w", encoding="utf-8") as f:
            f.write(json_data)

        # Success!
        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
