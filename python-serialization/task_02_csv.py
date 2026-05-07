#!/usr/bin/python3
import csv
import json


df convert_csv_to_json(filename):
    try:
        data = []

        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True

    except Exception:
        return False
