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
        print(f"Color: {note.color}")
        if note.tags:
            print(f"Tags: {', '.join(note.tags)}")
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
        print("5. Search notes")
        print("6. Search by tag")
        print("7. Search by color")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == "1":
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            color = input("Enter note color (or press Enter for white): ").strip() or "white"
            tags = input("Enter tags (comma-separated, or press Enter for none): ").strip()
            tags = [tag.strip() for tag in tags.split(",")] if tags else []
            new_note = Note(title=title, content=content, color=color, tags=tags)
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
                        new_color = input("Enter new color (press Enter to keep current): ")
                        new_tags = input("Enter new tags (comma-separated, press Enter to keep current): ")
                        
                        if new_title:
                            note.title = new_title
                        if new_content:
                            note.content = new_content
                        if new_color:
                            note.color = new_color
                        if new_tags:
                            note.tags = [tag.strip() for tag in new_tags.split(",")]
                            
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
            query = input("Enter search query: ")
            found_notes = note_list.search_notes(query)
            display_notes(found_notes)
            
        elif choice == "6":
            tag = input("Enter tag to search for: ")
            found_notes = note_list.get_notes_by_tag(tag)
            display_notes(found_notes)
            
        elif choice == "7":
            color = input("Enter color to search for: ")
            found_notes = note_list.get_notes_by_color(color)
            display_notes(found_notes)
            
        elif choice == "8":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()