# README.md

# Note Bot

Note Bot is a simple note-taking application that allows users to create, save, and manage their notes efficiently. This project is built using Python and provides a straightforward interface for handling notes.

## Features

- Create and save notes with titles and content.
- Retrieve and display all saved notes.
- Delete notes as needed.
- Persistent storage using SQLite.

## Project Structure

```
note-bot
├── src
│   ├── main.py                # Entry point of the application
│   ├── components
│   │   ├── note.py            # Note class definition
│   │   └── note_list.py       # NoteList class for managing notes
│   ├── utils
│   │   └── file_handler.py     # Utility functions for file operations
│   └── database
│       └── notes.db           # SQLite database for storing notes
├── tests
│   ├── test_note.py           # Unit tests for Note class
│   └── test_file_handler.py    # Unit tests for file handling functions
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd note-bot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

Follow the on-screen instructions to create and manage your notes.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you'd like to add.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.