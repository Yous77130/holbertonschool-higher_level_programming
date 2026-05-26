#!/usr/bin/env python3
"""Module for serializing and deserializing with XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file.

    Args:
        dictionary: Python dictionary to serialize
        filename: output XML filename
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize a dictionary from an XML file.

    Args:
        filename: input XML filename

    Returns:
        Python dictionary with deserialized data
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    return {child.tag: child.text for child in root}
