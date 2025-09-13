# filepath: note-bot/src/main.py

from components.note import Note
from components.note_list import NoteList
from utils.file_handler import load_notes, save_notes

def display_notes(notes):
    if not notes:
        print("No notes found!")
        return False
    shown = 0
    for note in notes:
        if not note.title.strip() and not note.content.strip():
            continue
        shown += 1
        print(f"\nNote {shown}:")
        print(f"Title: {note.title}")
        print(f"Content: {note.content}")
        if note.tags:
            print(f"Tags: {', '.join(note.tags)}")
        if hasattr(note, 'tasks') and note.tasks:
            print("Tasks:")
            for idx, task in enumerate(note.tasks, 1):
                check = '[x]' if task.get('done') else '[ ]'
                print(f"  {idx}. {check} {task.get('text','')}")
    if shown == 0:
        print("No notes found!")
        return False
    return True
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
        print("7. Add task to note")
        print("8. Toggle task checkbox")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            tags = input("Enter tags (comma-separated, or press Enter for none): ").strip()
            tags = [tag.strip() for tag in tags.split(",")] if tags else []
            new_note = Note(title=title, content=content, tags=tags)
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
                        new_tags = input("Enter new tags (comma-separated, press Enter to keep current): ")
                        if new_title:
                            note.title = new_title
                        if new_content:
                            note.content = new_content
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
            notes = note_list.get_all_notes()
            if display_notes(notes):
                try:
                    index = int(input("\nEnter note number to add a task to: ")) - 1
                    if 0 <= index < len(notes):
                        task_text = input("Enter task description: ")
                        notes[index].add_task(task_text)
                        save_notes(note_list.get_all_notes())
                        print("Task added!")
                    else:
                        print("Invalid note number!")
                except ValueError:
                    print("Please enter a valid number!")

        elif choice == "8":
            notes = note_list.get_all_notes()
            if display_notes(notes):
                try:
                    note_index = int(input("\nEnter note number to toggle a task: ")) - 1
                    if 0 <= note_index < len(notes):
                        note = notes[note_index]
                        if not hasattr(note, 'tasks') or not note.tasks:
                            print("No tasks for this note.")
                        else:
                            for idx, task in enumerate(note.tasks, 1):
                                check = '[x]' if task.get('done') else '[ ]'
                                print(f"  {idx}. {check} {task.get('text','')}")
                            task_index = int(input("Enter task number to toggle: ")) - 1
                            if 0 <= task_index < len(note.tasks):
                                note.toggle_task(task_index)
                                save_notes(note_list.get_all_notes())
                                print("Task checkbox toggled!")
                            else:
                                print("Invalid task number!")
                    else:
                        print("Invalid note number!")
                except ValueError:
                    print("Please enter a valid number!")

        elif choice == "9":
            print("Goodbye!")
            return

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()