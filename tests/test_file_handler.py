import unittest
from src.utils.file_handler import load_notes, save_notes

class TestFileHandler(unittest.TestCase):

    def test_load_notes(self):
        # Assuming a test file 'test_notes.json' exists with sample notes
        notes = load_notes('test_notes.json')
        self.assertIsInstance(notes, list)
        self.assertGreater(len(notes), 0)

    def test_save_notes(self):
        notes = [{'title': 'Test Note', 'content': 'This is a test note.'}]
        save_notes(notes, 'test_output_notes.json')
        loaded_notes = load_notes('test_output_notes.json')
        self.assertEqual(notes, loaded_notes)

if __name__ == '__main__':
    unittest.main()