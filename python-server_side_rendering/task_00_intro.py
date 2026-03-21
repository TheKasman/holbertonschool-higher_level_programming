#!/usr/bin/python3
"""Question 1"""

import os

def generate_invitations(template, attendees):
    """Generate a personaized invitation"""

    #  Input validation
    #  Bad input
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    #  Empty input
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    #  Assign varibles to output then write
    for i, attendee in enumerate(attendees, start=1):
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        output = template
        output = output.replace("{name}", name)
        output = output.replace("{event_title}", event_title)
        output = output.replace("{event_date}", event_date)
        output = output.replace("{event_location}", event_location)

        filename = f"output_{i}.txt"

        if os.path.exists(filename):
            print(f"Warning: {filename} already exists and will be overwritten")

        with open(filename, "w", encoding='utf-8') as f:
            f.write(output)
