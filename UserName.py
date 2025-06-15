def check(UserName):
    if len(UserName)>12 or UserName.find(" ") or UserName.isdigit():
        return "Username in valid\nUsername must be 12 characters or less\nUsername must not have space in them\nUsername must not contain digits"
    else:
        return "{UserName} Valid Username"
def main():
    UserName = input("Enter your username: ")
    print(check(UserName))
main()