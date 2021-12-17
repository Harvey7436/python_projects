def main():
    email_list = {}
    email = input("Please enter your email: ")
    while email != "":
        name = get_name(email)
        confirmation = input("Is your name {}? (Y/n) ".format(name))
        if confirmation.upper() == "n":
            name = input("Name: ")
        email_list[email] = name
        email = input("Email: ")

    for email, name in email_list.items():
        print("{} ({})".format(name, email))


def get_name(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()