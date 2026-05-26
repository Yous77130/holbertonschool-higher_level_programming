#!/usr/bin/env python3
"""Module for basic serialization and deserialization."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file.

    Args:
        data: Python dictionary to serialize
        filename: output JSON filename
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize data from a JSON file.

    Args:
        filename: input JSON filename

    Returns:
        Python dictionary with deserialized data
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
