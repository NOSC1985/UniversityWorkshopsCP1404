
userName = input("Please enter your name: ")

menu = ("(H)ello\n(G)oodbye\n(Q)uit")
print(menu)
print()

chosenMenuOption = input('Input your selection: ')

while chosenMenuOption != 'Q':

    if chosenMenuOption == 'H':

        print("Hello", userName)

    elif chosenMenuOption == 'G':

        print('Goodbye,', userName)

    else:

        print("Invalid choice")

    print(menu)
    print()

    chosenMenuOption = input('Input your selection: ')

print("Finished")