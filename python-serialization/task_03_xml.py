#!/usr/bin/python3
"""XML time"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize time"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        #  Key becomes the tag
        child = ET.SubElement(root, key)
        #  Value becomes the text inside the tag
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8")


def deserialize_from_xml(filename):
    """Deserialization"""
    tree = ET.parse(filename)
    root = tree.getroot()

    #  Convert XML -> Dictionary
    data_from_xml = {child.tag: child.text for child in root}

    #  Data type conversion
    if "age" in data_from_xml:
        data_from_xml["age"] = int(data_from_xml["age"])

    return data_from_xml
