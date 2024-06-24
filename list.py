acronyms = ["LOL", "IDK", "SMH", "TBH"]
print(acronyms[0])

acronyms.append("LMAO")
print(acronyms[4])

numbers = [1,2,3,4,5,6]
if 8 in numbers:
    print("This number is in the list")
else:
    print("This number is not in the list")

word = "LMAO"
if word in acronyms:
    print("Yes, " + word + " is contained in the acronyms list.")
else: 
    print("No, this acronym is not in the list")

for acronym in acronyms:
    print(acronym)