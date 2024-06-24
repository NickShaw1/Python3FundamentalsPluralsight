contact = {
    "numbers":"4",
    "students":
        [
            {'name': "Nick Shaw", "email": "nickshaw@qub.ac.uk"},
            {'name': "Debbie Henry", "email": "debs07@qub.ac.uk"},
            {"name": "Eva Henry-Shaw", "email": "eva@qub.ac.uk"},
        ]
}

print("Student emails:")
for student in contact["students"]:
    print(student["email"])