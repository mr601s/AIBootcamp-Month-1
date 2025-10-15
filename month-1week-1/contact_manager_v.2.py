import json
from datetime import datetime

# Global contacts list
contacts = []

def safe_input(prompt: str):
    """Input helper that returns None on EOF/interrupt instead of crashing."""
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        return None

def get_timestamp():
    """Get current timestamp in ISO format"""
    return datetime.now().isoformat()

def save_contacts():
    """Save contacts to JSON file"""
    try:
        with open('contacts_v2.json', 'w') as file:
            json.dump(contacts, file, indent=4)
        print("✅ Contacts saved!")
    except Exception as e:
        print(f"❌ Error saving: {e}")

def load_contacts():
    """Load contacts from JSON file"""
    global contacts
    try:
        with open('contacts_v2.json', 'r') as file:
            contacts = json.load(file)
        print(f"✅ Loaded {len(contacts)} contacts")
    except FileNotFoundError:
        print("📝 No saved contacts. Starting fresh!")
        contacts = []
    except Exception as e:
        print(f"❌ Error loading: {e}")
        contacts = []

def add_contact():
    """Add a new contact with enhanced fields"""
    print("\n" + "="*50)
    print("📇 ADD NEW CONTACT")
    print("="*50)
    
    # Basic info
    name = safe_input("\nName: ")
    if name is None:
        print("\nOperation cancelled.")
        return
    category = input("Category (Work/Personal/Family): ").capitalize()
    
    # Emails
    print("\n--- Email Addresses ---")
    email_personal = input("Personal email (or press Enter to skip): ")
    email_work = input("Work email (or press Enter to skip): ")
    
    # Phones
    print("\n--- Phone Numbers ---")
    phone_mobile = input("Mobile (or press Enter to skip): ")
    phone_home = input("Home (or press Enter to skip): ")
    phone_work = input("Work (or press Enter to skip): ")
    
    # Address
    print("\n--- Address ---")
    add_address = input("Add address? (y/n): ").lower()
    address = {}
    if add_address == 'y':
        address = {
            "street": input("Street: "),
            "city": input("City: "),
            "state": input("State: "),
            "zip": input("ZIP: ")
        }
    
    # Notes
    notes = input("\nNotes (optional): ")
    
    # Favorite
    favorite = input("Mark as favorite? (y/n): ").lower() == 'y'
    
    # Build the contact dictionary
    contact = {
        "name": name,
        "category": category,
        "favorite": favorite,
        "created_at": get_timestamp(),
        "modified_at": get_timestamp(),
        "emails": {},
        "phones": {},
        "address": address,
        "notes": notes
    }
    
    # Add emails if provided
    if email_personal:
        contact["emails"]["personal"] = email_personal
    if email_work:
        contact["emails"]["work"] = email_work
    
    # Add phones if provided
    if phone_mobile:
        contact["phones"]["mobile"] = phone_mobile
    if phone_home:
        contact["phones"]["home"] = phone_home
    if phone_work:
        contact["phones"]["work"] = phone_work
    
    contacts.append(contact)
    save_contacts()
    print(f"\n✅ Added {name} to contacts!")

def view_contacts():
    """Display all contacts with enhanced formatting"""
    if not contacts:
        print("\n📭 No contacts yet!")
        return
    
    print("\n" + "="*60)
    print(f"📇 YOUR CONTACTS ({len(contacts)} total)")
    print("="*60)
    
    for i, contact in enumerate(contacts, 1):
        # Show star if favorite
        star = "⭐" if contact.get("favorite", False) else "  "
        print(f"\n{star} {i}. {contact.get('name', 'Unnamed')} [{contact.get('category', 'N/A')}]")
        
        # Display emails
        if contact.get("emails"):
            print("   📧 Emails:")
            for email_type, email in contact["emails"].items():
                print(f"      {email_type}: {email}")
        
        # Display phones
        if contact.get("phones"):
            print("   📱 Phones:")
            for phone_type, phone in contact["phones"].items():
                print(f"      {phone_type}: {phone}")
        
        # Display address
        if contact.get("address") and contact["address"]:
            addr = contact["address"]
            street = addr.get('street', '')
            city = addr.get('city', '')
            state = addr.get('state', '')
            zip_code = addr.get('zip', '')
            print(f"   🏠 Address: {street}, {city}, {state} {zip_code}")
        
        # Display notes
        if contact.get("notes"):
            print(f"   📝 Notes: {contact['notes']}")
        
        # Display creation date
        created = contact.get("created_at", "Unknown")
        print(f"   🕐 Added: {created[:10]}")

def view_by_category():
    """View contacts filtered by category"""
    if not contacts:
        print('\n No contacts yet!')
        return 
    
    print('\n--- Filter by category ---')
    print('1. Work')
    print('2. Personal')
    print('3. Family')
    print('4. All')
          
    choice = safe_input('\nChoose category: ')
    if choice is None:
        print('Operation cancelled.')
        return

    category_map = {
        '1': 'Work',
        '2': 'Personal',
        '3': 'Family',
        '4': 'All'
    }

    category = category_map.get(choice, 'All')

    # Filter contacts using list comprehension
    if category == 'All':
        filtered = contacts
    else:
        filtered = [c for c in contacts if c.get('category') == category]

    if not filtered:
        print(f"\n No contacts in '{category}' category")
        return

    print('\n' + '='*60)
    print(f"Contacts in {category} ({len(filtered)} total)")
    print('='*60)

    for contact in filtered:
        star = '★' if contact.get('favorite') else ' '
        print(f'\n{star} {contact["name"]}')
        if contact.get('emails'):
            print(' Emails:')
            for email_type, email in contact['emails'].items():
                print(f'  - {email_type.capitalize()}: {email}')
        if contact.get('phones'):
            first_phone = list(contact['phones'].values())[0]
            print(f' Phone: {first_phone}')

def view_favorites():
    """Display only favorite contacts"""
    # Filter using list comprehension
    favorites = [c for c in contacts if c.get('favorite', False)]

    if not favorites:
        print('\n⭐ No favorite contacts yet!')
        return
    
    print('\n' + '='*60)
    print(f'⭐ YOUR FAVORITE CONTACTS ({len(favorites)} total)')
    print('='*60)

    for contact in favorites:
        print(f"⭐ {contact['name']} [{contact.get('category', 'N/A')}]")
        if contact.get('emails'):
            print(f" {list(contact['emails'].values())[0]}")
        if contact.get('phones'):
            print(f" {list(contact['phones'].values())[0]}")

def search_contacts():
    """Search contacts across all fields!"""
    if not contacts:
        print('\n No contacts to search!')
        return

    term = safe_input('\nEnter search term: ')
    if term is None:
        print('Operation cancelled.')
        return
    search_term = term.lower()
    found = []

    for contact in contacts:
        # Search in name
        if search_term in contact.get('name', '').lower():
            found.append(contact)
            continue

        # Search in category
        if search_term in contact.get('category', '').lower():
            found.append(contact)
            continue

        # Search in emails
        for email in contact.get('emails', {}).values():
            if search_term in email.lower():
                found.append(contact)
                break
        else:
            # Search in phones only if not already found via emails
            for phone in contact.get('phones', {}).values():
                if search_term in phone.lower():
                    found.append(contact)
                    break

    if not found:
        print("\n No matches found.")
        return

    print('\n' + '='*60)
    print(f"🔎 Search results for '{search_term}' ({len(found)} matches)")
    print('='*60)
    for c in found:
        star = '★' if c.get('favorite') else ' '
        print(f"{star} {c.get('name', 'Unnamed')} [{c.get('category', 'N/A')}]")


def delete_contact():
    """Delete a contact"""
    if not contacts:
        print('\n No contacts to delete!')
        return
    
    view_contacts()

    try:
        raw = safe_input('\nEnter contact number to delete (0 to cancel): ')
        if raw is None:
            print('Delete cancelled')
            return
        choice = int(raw)

        if choice == 0:
            print('Delete cancelled')
            return
        
        if 1 <= choice <= len(contacts):
            deleted = contacts.pop(choice - 1)
            save_contacts()
            print(f"\n🗑️ Deleted {deleted['name']} from contacts.")
        else:
            print('Invalid choice.')
    except ValueError:
        print('Invalid input. Please enter a number.')

def main():
    """Main program loop"""
    load_contacts()

    while True:
        print('\n' + '='*60)
        print('Contact Manager v2.0')
        print('='*60)
        print('1. Add Contact')
        print('2. View all contacts')
        print('3. View by category')
        print('4. View favorites')
        print('5. Search contacts')
        print('6. Delete contact')
        print('0. Exit')

        choice = input('\nEnter your choice: ')

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            view_by_category()
        elif choice == '4':
            view_favorites()
        elif choice == '5':
            search_contacts()
        elif choice == '6':
            delete_contact()
        elif choice == '0':
            print('Goodbye!')
            break
        else:
            print('Invalid choice.')

if __name__ == "__main__":
    main()cont
