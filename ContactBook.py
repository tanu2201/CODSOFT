contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")

    if name and phone:
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print("Contact added successfully!")

def view_contacts():
    for name, details in contacts.items():
        print(f"{name} - {details['phone']}")

def search_contact():
    search_term = input("Enter search term: ")
    found_contacts = []
    for name, details in contacts.items():
        if search_term in name or search_term in details["phone"]:
            found_contacts.append(f"{name} - {details['phone']}")
    if found_contacts:
        print("Search results:")
        for contact in found_contacts:
            print(contact)
    else:
        print("No contacts found.")

def update_contact():
    name = input("Enter contact name: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print("Contact updated successfully!")

def delete_contact():
    name = input("Enter contact name: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")

def main():
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    
