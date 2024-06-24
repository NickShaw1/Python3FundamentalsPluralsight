acronyms = {'LOL': 'Laugh out loud',
            'LMAO': 'Laugh my a** off',
            'ROFL': 'Rolling on the floor laughing'}

definition = acronyms.get("LOL")

if definition:
    print(definition)

else:
    print("This acronym does not exist")