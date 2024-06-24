acronyms = {'LOL': 'Laugh out loud',
            'LMAO': 'Laugh my a** off',
            'ROFL': 'Rolling on the floor laughing'}

print("The list of acronyms includes 'LOL', 'LMAO' and 'ROFL'")

user_choice = input("What acronym do you want to enter? ")

if user_choice == 'LOL':
    print(acronyms['LOL'])
elif user_choice == 'LMAO':
    print(acronyms['LMAO'])
elif user_choice == 'ROFL':
    print(acronyms['ROFL'])

else:
    print("You did not select any of the listed acronyms.")
    choice2 = input("Would you like to try again? Please select Yes or No. " )

    if choice2 == "Yes":
        print("Too late, you had your chance.") 

    if choice2 == "No":
        print("Good, I didn't want you to anyway.")
    
    else:
        print("So, what are you telling me for?")