# Day 4: Note- taking App with File Persistence

from fileinput import filename
import os
from datetime import datetime

# ========== Core Note Functions ==========

def create_note(title, content):
    """
    Create a new note and save it to a file
    Filename format: note_TITLE.txt
    """
    # Create safe filename (remove spaces, special chars)
    filename = f"note_{title.replace(' ', '_')}.txt"

    # Get current timestamp
    timestamp = datetime.now().strftime('%y-%m-%d %H:%M:%S')

    # Write note to file with timestamp
    with open(filename, 'w') as file:
        file.write(f"Title: {title}\n")
        file.write(f"Created: {timestamp}\n")
        file.write('-' * 50 + '\n\n')
        file.write(content)

    print(f'Note saved: {filename}')
    return filename

def read_note(filename):
    """
    Read and display a note from file
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print('\n' + '='*50)
            print(content)
            print('='*50 + '\n')
            return content
    except FileNotFoundError:
        print(f'Note not found: {filename}')
        return None
    
def list_all_notes():
    """
    List all note files in current directory
    Returns list of notes filenames
    """

    # Get all files in current directory
    all_files = os.listdir('.')

    # Filter for note files (start with 'note_' and end with '.txt')
    note_files = [f for f in all_files if f.startswith('note_') and f.endswith('.txt')]

    if len(note_files) == 0:
        print('\n No notes found.\n')
        return []
    
    print('\n' + '='*50)
    print('Your Notes')
    print('='*50)
    for i, filename in enumerate(note_files, 1):
        # Extract title from filename
        title = filename.replace('note_', '').replace('.txt', '').replace('_', ' ')
        print(f' {i}. {title}')
    print('='*50 + '\n')

    return note_files

def delete_note(filename):
    '''
    Delete a note file
    '''
    try:
        os.remove(filename)
        print(f'Note deleted: {filename}')
        return True
    except FileNotFoundError:
        print(f'Note not found: {filename}')
        return False
    
def search_notes(keyword):
    """
    Search all notes for a keyword
    Returns list of matching filenames
    """
    note_files = list_all_notes()
    matches = []

    keyword_lower = keyword.lower()

    for filename in note_files:
        with open(filename, 'r') as file:
            content = file.read().lower()
            if keyword_lower in content:
                matches.append(filename)

    if len(matches) == 0:
        print(f'\n No notes found containing: {keyword}\n')
    else:
        print(f'\n Found {len(matches)} note(s) containing "{keyword}":')
        for filename in matches:
            title = filename.replace('note_', '').replace('.txt', '').replace('_', ' ')
            print(f' - {title}')
        print()

    return matches

import os
# os.listdir('.') # Lists all files in the current directory
# os.remove("filename") # Deletes a file

from datetime import datetime
# datetime.now() # Gets current date and time
# .strftime('%y-%m-%d %H:%M:%S') # Formats it as a string

# Example: List comprehension to filter note files
# all_files = os.listdir('.')
# note_files = [f for f in all_files if f.startswith('note_')]

# Example: Traditional loop approach
# note_files = []
# for f in all_files:
#     if f.startswith('note'):
#         note_files.append(f)

# ========== Interactive Menu System ==========
def display_menu():
    """Display the main menu"""
    print('\n' + '='*50)
    print('Note-Taking App')
    print('='*50)
    print('\n Commands:')
    print(' create - Create a new note')
    print(' list - List all notes')
    print(' read - Read a specific note')
    print(' search - Search notes by keyword')
    print(' delete - Delete a note')
    print(' help - Show this menu')
    print(' quit - Exit Application')
    print('='*50 + '\n')

def get_user_input(prompt):
    """Get input from user with consistent formatting"""
    return input(f' {prompt}: ').strip()

def interactive_notes_app():
    """
    Main interactive note-taking application
    """
    display_menu()

    while True:
        command = get_user_input('Enter command').lower()

        # Quit Command
        if command == 'quit':
            print('\nThank you for using the Note-Taking App!')
            print('All of your notes are saved.\n')
            break
    
        # Help Command
        elif command == 'help':
            display_menu()
        
        # List Command
        elif command == 'list':
            list_all_notes()

        # Create Command
        elif command == 'create':
            print('\n --- Create a New Note ---')
            title = get_user_input('Note title')

            if not title:
                print('Error: Title cannot be empty!')
                continue

            print('Enter note content (type "DONE" on a new line when finished):')
            content = []
            while True:
                line = input(' ')
                if line == 'DONE':
                    break
                content.append(line)

            content = '\n'.join(content)

            if not content:
                print('Error: Note content cannot be empty!')
                continue

            create_note(title,content)

        # Read Command
        elif command == 'read':
            notes = list_all_notes()
        
            if len(notes) == 0:
                continue
        
            try:
                choice = int(get_user_input('Enter note number to read'))
                if 1 <= choice <= len(notes):
                    read_note(notes[choice - 1])
                else:
                    print(f' Please enter a number between 1 and {len(notes)}\n')
            except ValueError:
                print(' Error: Please enter a valid number!\n')

        # Search Command
        elif command == 'search':
            keyword = get_user_input('Enter keyword to search for')
            if keyword:
                matches = search_notes(keyword)

                if len(matches) > 0:
                    view = get_user_input('View a note? (yes/no)').lower()
                    if view == 'yes':
                        try:
                            choice = int(get_user_input('Enter note number to read'))
                            if 1 <= choice <= len(matches):
                                read_note(matches[choice - 1])
                            else:
                                print(f' Please enter a number between 1 and {len(matches)}\n')
                        except ValueError:
                            print(' Error: Please enter a valid number!\n')

        # Delete Command
        elif command == 'delete':
            notes = list_all_notes()

            if len(notes) == 0:
                continue

            try:
                choice = int(get_user_input('Enter note number to delete'))
                if 1 <= choice <= len(notes):
                    filename = notes[choice - 1]
                    title = filename.replace('note_', '').replace('.txt', '').replace('_', ' ')

                    confirm = get_user_input(f'Delete "{title}"? (yes/no)').lower()
                    if confirm == 'yes':
                        delete_note(filename)
                    else:
                        print('\n Deletion cancelled.\n')
                else:
                    print(f' Please enter a number between 1 and {len(notes)}\n')
            except ValueError:
                print('Error: Please enter a valid number\n')

        # Unknown Command 
        else:
            print('Error: Unknown command! Type "help" for menu.\n')

if __name__ == "__main__":
    # Uncomment this for testing:
    # print("=== Note-Taking App Test ===\n")
    # create_note("My First Note", "This is the content of my first note.\nIt can have multiple lines!")
    # create_note("Shopping List", "Milk\nBread\nEggs\nCoffee")
    # notes = list_all_notes()
    # if len(notes) > 0:
    #     read_note(notes[0])
    # search_notes("first")
    
    # Run interactive application
    interactive_notes_app()
    