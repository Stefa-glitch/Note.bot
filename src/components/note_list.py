from typing import List
from components.note import Note

class NoteList:
    def __init__(self):
        self.notes: List[Note] = []
    
    def add_note(self, note: Note) -> None:
        self.notes.append(note)
    
    def get_all_notes(self) -> List[Note]:
        return self.notes
        
    def delete_note(self, index: int) -> None:
        if 0 <= index < len(self.notes):
            self.notes.pop(index)
