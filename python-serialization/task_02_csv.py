#!/usr/bin/env python3
"""Module for converting CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON format.

    Args:
        csv_filename: input CSV filename

    Returns:
        True if successful, False otherwise
    """
    try:
        with open(csv_filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f)
        return True
    except FileNotFoundError:
        return False
