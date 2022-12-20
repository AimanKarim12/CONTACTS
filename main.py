#CONTACT ASSIGNMENT
contacts = []  # list to store all the contacts

loop = True
while loop:
    # Display the main menu
    print("Main Menu")
    print("1. Display Contact Names")
    print("2. Search for Contact")
    print("3. Edit Contact")
    print("4. New Contact")
    print("5. Remove Contact")
    print("6. Exit")

    # Get the user's choice
    choice = int(input("Enter Selection (1-6): "))

    if choice == 1:
        # Display all contact names
        for contact in contacts:
            print(contact['name'])

    elif choice == 2:
        # Search for a contact
        name = input("Which contact would you like to search for?: ")
        found = False 
        for contact in contacts:
            if contact['name'] == name:
                found = True
                print("Name:", contact['name'])
                print("Phone:", contact['phone'])
                print("Email:", contact['email'])
                break
        if not found:
            print("Contact not found")

    elif choice == 3:
        # Edit a contact
        name = input("Select a contact to edit: ")
        found = False 
        for contact in contacts:
            if contact['name'] == name:
                found = True
                # Update the contact information
                contact['name'] = input("Enter the new name: ")
                contact['phone'] = input("Enter the new phone number: ")
                contact['email'] = input("Enter the new email address: ")
                break
        if not found:
            print("Contact not found")

    elif choice == 4:
        # Add a new contact
        name = input("Enter the name of the new contact: ")
        phone = input("Enter the phone number of the new contact: ")
        email = input("Enter the email address of the new contact: ")

        contacts.append({'name': name, 'phone': phone, 'email': email})

    elif choice == 5:
        # Remove a contact
        name = input("Select a contact to remove: ")
        found = False  
        for i, contact in enumerate(contacts):
            if contact['name'] == name:
                found = True
                # Remove the contact from the list
                del contacts[i]
                break
        if not found:
            print("Contact not found")

    elif choice == 6:
        # Exit the program
        loop = False
    
