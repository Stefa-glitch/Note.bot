import unittest
from src.components.note import Note

class TestNote(unittest.TestCase):

    def setUp(self):
        self.note = Note(title="Test Title", content="Test Content")

    def test_save(self):
        self.note.save()
        # Add assertions to verify the note is saved correctly

    def test_delete(self):
        self.note.save()
        self.note.delete()
        # Add assertions to verify the note is deleted correctly

if __name__ == '__main__':
    unittest.main()