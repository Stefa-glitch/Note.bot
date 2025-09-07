# filepath: note-bot/src/main.py

from components.note import Note
from components.note_list import NoteList
from utils.file_handler import load_notes, save_notes

def display_notes(notes):
    if not notes:
        print("No notes found!")
        return False
    for i, note in enumerate(notes, 1):
        print(f"\nNote {i}:")
        print(f"Title: {note.title}")
        print(f"Content: {note.content}")
    return True

def main():
    note_list = NoteList()
    notes = load_notes()
    
    for note in notes:
        note_list.add_note(note)

    while True:
        print("\n=== Note Bot ===")
        print("1. Add new note")
        print("2. View all notes")
        print("3. Edit note")
        print("4. Delete note")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            new_note = Note(title=title, content=content)
            note_list.add_note(new_note)
            save_notes(note_list.get_all_notes())
            print("Note added successfully!")
            
        elif choice == "2":
            notes = note_list.get_all_notes()
            display_notes(notes)
                    
        elif choice == "3":
            notes = note_list.get_all_notes()
            if display_notes(notes):
                try:
                    index = int(input("\nEnter note number to edit: ")) - 1
                    if 0 <= index < len(notes):
                        note = notes[index]
                        print("\nCurrent note details:")
                        print(f"Title: {note.title}")
                        print(f"Content: {note.content}")
                        
                        new_title = input("\nEnter new title (press Enter to keep current): ")
                        new_content = input("Enter new content (press Enter to keep current): ")
                        
                        if new_title:
                            note.title = new_title
                        if new_content:
                            note.content = new_content
                            
                        save_notes(note_list.get_all_notes())
                        print("Note updated successfully!")
                    else:
                        print("Invalid note number!")
                except ValueError:
                    print("Please enter a valid number!")
                    
        elif choice == "4":
            notes = note_list.get_all_notes()
            if display_notes(notes):
                try:
                    index = int(input("\nEnter note number to delete: ")) - 1
                    if 0 <= index < len(notes):
                        note_list.delete_note(index)
                        save_notes(note_list.get_all_notes())
                        print("Note deleted successfully!")
                    else:
                        print("Invalid note number!")
                except ValueError:
                    print("Please enter a valid number!")
                    
        elif choice == "5":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()