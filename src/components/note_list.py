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
            
    def search_notes(self, query: str) -> List[Note]:
        query = query.lower()
        return [note for note in self.notes 
                if query in note.title.lower() 
                or query in note.content.lower()
                or any(query in tag.lower() for tag in note.tags)]
    
    def get_notes_by_tag(self, tag: str) -> List[Note]:
        return [note for note in self.notes if tag in note.tags]
    
    def get_notes_by_color(self, color: str) -> List[Note]:
        return [note for note in self.notes if note.color.lower() == color.lower()]
