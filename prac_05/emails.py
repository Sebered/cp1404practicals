def main():
    email_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        confirm = input(f"Is your name {name}? (Y/n) ")
        if confirm.upper() != "Y" and confirm != "":
            name = input("Name: ")
        email_name[email] = name
        email = input("Email: ")

    for email, name in email_name.items():
        print(f"{name} ({email})")


def get_name(email):
    first_half = email.split('@')[0]
    name_parts = first_half.split('.')
    name = " ".join(name_parts).title()
    return name


main()