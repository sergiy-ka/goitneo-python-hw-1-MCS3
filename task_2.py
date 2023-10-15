# Homework-1 >>> CLI-bot
def add_contact(args, contacts):
    if len(args) != 2:
        res = "Incorrect format! Valid format is: add [name] [contact]"
    else:
        name, phone = args
        if contacts.get(name) != None:
            res = "Name already exists!"
        else:
            contacts[name] = phone
            res = "Contact added."
    return res


def change_contact(args, contacts):
    if len(args) != 2:
        res = "Incorrect format! Valid format is: change [name] [new contact]"
    else:
        name, phone = args
        if contacts.get(name) == None:
            res = "Name is not found in the contact list."
        else:
            contacts.update({name: phone})
            res = "Contact changed."
    return res


def show_phone(args, contacts):
    if len(args) != 1:
        res = "Incorrect format! Valid format is: phone [name]"
    else:
        name = args[0]
        res = contacts.get(name) if contacts.get(
            name) else "Name is not found in the contact list."
    return res


def show_all(contacts):
    contact_list = []
    if len(contacts) == 0:
        return "Contact list is empty."
    for k, v in contacts.items():
        contact_line = k + ": " + v
        contact_list.append(contact_line)
    return ("\n").join(contact_list)


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command in ["hello", "hi"]:
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
