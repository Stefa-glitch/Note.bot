# filepath: note-bot/src/components/note.py

class Note:
    def __init__(self, title, content, tags=None, tasks=None):
        self.title = title
        self.content = content
        self.tags = tags or []
        self.tasks = tasks or []  # Each task: {"text": str, "done": bool}

    def add_task(self, text):
        self.tasks.append({"text": text, "done": False})

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def toggle_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = not self.tasks[index]["done"]

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)


    def save(self):
        # Logic to save the note to the database
        pass

    def delete(self):
        # Logic to delete the note from the database
        pass