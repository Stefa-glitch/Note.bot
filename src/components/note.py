# filepath: note-bot/src/components/note.py

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def save(self):
        # Logic to save the note to the database
        pass

    def delete(self):
        # Logic to delete the note from the database
        pass