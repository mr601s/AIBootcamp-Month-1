# Day 4: File I/O and Data Persistence

# ========= Basic File Operations =========

def write_simple_files():
    """
    Create a file and write text to it
    This is the simplest form of file writing
    """

    # Open file in write mode ('w')
    # If file doesn't exist. Python creates it
    # If it does exist, Python overwrites it
    file = open('test.txt', 'w')

    # Write some text
    file.write('Hello, this is my first file!\n')
    file.write('Python can save data.\n')

    # CRITICAL: Always close the file 
    file.close()

    print(" File Created: test.txt")


def read_simple_file():
    """
    Open a file and read its contents
    """
    # Open file in read mode ('r')
    file = open('test.txt', 'r')

    # Read entire file as one string 
    content = file.read()

    # Close the file
    file.close()

    print("File contents:")
    print(content)
    return content 

def write_with_context_manager():
    """
    The Correct way to work with files
    'with' automatically closes the file, even if errors occur
    """
    with open('better_test.txt', 'w') as file:
        file.write('This is the professional way to handle files.\n')
        file.write('The file automatically closes when done.\n')

    # File is already closed here - no need to call file.close()
    print('File created with context manager')

def read_with_context_manager():
    """
    Reading with context manager
    """
    with open('better_test.txt', 'r') as file:
        content = file.read()

        print('File contents:')
        print(content)
        return content
    
def demonstrate_append_mode():
    """
    Show how append mode works
    """
    
    # Create initial file
    with open('append_test.txt', 'w') as file:
        file.write('First line\n')
        file.write('Second line\n')
    
    # Append to existing file
    with open('append_test.txt', 'a') as file:
        file.write('Third line\n')

    # Read the result
    with open('append_test.txt', 'r') as file:
        content = file.read()
        print('Appended file contents:')
        print(content)

def read_line_by_line():
    """
    Read and process each line individually
    Useful for large files
    """
    with open('test.txt', 'r') as file:
        # Method 1: readlines() - return list of all lines
        lines = file.readlines()

        print('Lines as a list:')
        for i, line in enumerate(lines, 1):
            print(f"{i}: {line.strip()}") # .strip() removes \n

    print()

    # Method 2: Iterates directly (more memory efficient)
    with open('test.txt', 'r') as file:
        print('Iterating directly:')
        for line in file:
            print(f' {line.strip()}')

# Test the basic operations 
if __name__ == "__main__":
    print("=== Basic File Operations ===\n")
    write_simple_files()
    read_simple_file()
    
    print("\n=== Better Way: Context Managers ===\n")
    write_with_context_manager()
    read_with_context_manager()

    #r Read from file
    read_simple_file()
    print("\n=== Append Mode Demo ===\n")
    demonstrate_append_mode()

    