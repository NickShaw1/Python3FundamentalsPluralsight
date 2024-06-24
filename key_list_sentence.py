acronyms = {'LOL': 'Laugh out loud',
            'LMAO': 'Laugh my a** off',
            'ROFL': 'Rolling on the floor laughing'}

sentence = "LOL" + ", " + "LMAO" + ' even.'
translation = acronyms.get("LOL") + ", " + acronyms.get("LMAO") + " even."

print("Sentence:", sentence)
print("Translation:", translation)