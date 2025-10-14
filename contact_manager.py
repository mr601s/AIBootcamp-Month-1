import json

# Our contacts will be stored in a list of dictionaries
contacts = []

def save_contacts():
    """Save contacts to JSON file"""
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)
    print('Contacts saved!')

def load_contacts():
    """Load contacts to JSON file"""
    global contacts
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
        print(f'Loaded {len(contacts)} contacts')
    except FileNotFoundError:
        print('No saved contacts found. Starting fresh!')
        contacts = []

def add_contacts():
    """Add a new contact"""
    print('\n--- Add New Contact ---')
    name = input('Name: ').strip()
    email = input('Email: ').strip()
    phone = input('Phone: ').strip()

    if not name:
        print('Name is required; contact not added.')
        return

    contact = {
        'name': name,
        'email': email,
        'phone': phone
    }
    contacts.append(contact)
    print(f"Added {name} to contacts!")

def view_contacts():
    """Display all contacts"""
    if not contacts:
        print('\nNo contacts yet!')
        return
    print('\n--- Your Contacts ---')
    for i, contact in enumerate(contacts, 1):
        print(f"\n{i}. {contact['name']}")
        print(f" Email: {contact['email']}")
        print(f" Phone: {contact['phone']}")

def delete_contact():
    """Delete a contact by its listed number"""
    if not contacts:
        print('\nNo contacts to delete!')
        return
    # Show all contacts with numbers
    view_contacts()

    try:
        choice_raw = input('\nEnter contact number to delete (0 to cancel): ').strip()
        if not choice_raw.isdigit():
            print('Please enter a valid number')
            return
        choice = int(choice_raw)
        if choice == 0:
            print('Delete cancelled')
            return
        if 1 <= choice <= len(contacts):
            deleted = contacts.pop(choice - 1)
            save_contacts()  # Auto-save after delete
            print(f"Deleted {deleted['name']} from contacts!")
        else:
            print('Invalid contact number')
    except ValueError:  # Fallback (kept for safety though we pre-check isdigit)
        print('Please enter a valid number')

def search_contacts():
    """Search for a contact by name, email, or phone"""
    if not contacts:
        print('\nNo contacts to search!')
        return
    
    search_term = input('\nEnter name, email, or phone to search: ').strip().lower()
    found = []

    for contact in contacts:
        # Search in name, email, AND phone
        if (search_term in contact['name'].lower() or
            search_term in contact['email'].lower() or
            search_term in contact['phone'].lower()):
            found.append(contact)

    if found:
        print(f"\nFound {len(found)} contact(s):")
        for c in found:
            print(f"\n Name: {c['name']}")
            print(f" Email: {c['email']}")
            print(f" Phone: {c['phone']}")
    else:
        print(f"\nNo contacts found matching '{search_term}'")

## Removed obsolete 'delere_contact' duplicate function


def main():
    """Main program loop"""
    load_contacts() # Load saved contacts when program starts

    while True:
        print('\n' + '=' * 40)
        print('Contact Manager')
        print('=' * 40)
        print('1. Add Contact')
        print('2. View All Contacts')
        print('3. Search Contacts')
        print('4. Delete Contact')
        print('5. Save and Exit')

        choice = input('\nChoose an option (1-5): ').strip()

        if choice == '1':
            add_contacts()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            save_contacts()
            print('Goodbye')
            break
        else:
            print('Invalid choice. Try again')

# Run the program
if __name__ == '__main__':
    main()