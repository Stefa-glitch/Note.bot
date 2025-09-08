import json
import os
from components.note import Note
from typing import List

def load_notes() -> List[Note]:
    file_path = "notes.json"
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, 'r') as file:
            notes_data = json.load(file)
            return [Note(
                title=note["title"],
                content=note["content"],
                tags=note.get("tags", []),
                color=note.get("color", "white")
            ) for note in notes_data]
    except:
        return []

def save_notes(notes: List[Note]) -> None:
    file_path = "notes.json"
    notes_data = [{
        "title": note.title,
        "content": note.content,
        "tags": note.tags,
        "color": note.color
    } for note in notes]
    with open(file_path, 'w') as file:
        json.dump(notes_data, file, indent=4)