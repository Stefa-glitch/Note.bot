# filepath: note-bot/src/components/note.py

class Note:
    def __init__(self, title, content, tags=None, color=None):
        self.title = title
        self.content = content
        self.tags = tags or []
        self.color = color or "white"

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)

    def set_color(self, color):
        self.color = color

    def save(self):
        # Logic to save the note to the database
        pass

    def delete(self):
        # Logic to delete the note from the database
        pass