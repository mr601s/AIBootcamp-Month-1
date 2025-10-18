import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from JSON file"""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    """Save contacts to JSON file"""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact"""
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    save_contacts(contacts)
    print(f"Contact {name} added successfully!")

def view_contacts(contacts):
    """Display all contacts"""
    if not contacts:
        print("No contacts found.")
        return
    
    print("\n=== All Contacts ===")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']}")

def search_contact(contacts):
    """Search for a contact by name"""
    name = input("Enter name to search: ")
    found = [c for c in contacts if name.lower() in c['name'].lower()]
    
    if found:
        print("\n=== Search Results ===")
        for contact in found:
            print(f"{contact['name']} - {contact['phone']} - {contact['email']}")
    else:
        print("No contacts found with that name.")

def delete_contact(contacts):
    """Delete a contact"""
    view_contacts(contacts)
    if not contacts:
        return
    
    try:
        index = int(input("\nEnter the number of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted = contacts.pop(index)
            save_contacts(contacts)
            print(f"Contact {deleted['name']} deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main program loop"""
    contacts = load_contacts()
    
    while True:
        print("\n=== Contact Manager ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
