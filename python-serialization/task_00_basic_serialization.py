#!/usr/bin/python3

"""No pickles here, neither is there dill"""
import json


def serialize_and_save_to_file(data, filename):
    """I'm super Serialized"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Okay maybe we need to deserialize the situation"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
