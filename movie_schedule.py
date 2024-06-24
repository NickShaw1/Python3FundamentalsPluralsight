current_movies = {"Dune 2": "7:00PM",
                 "Megalopolis": "8:00PM",
                 "Drive": "9:00PM",
                 "Titane": "10:00PM"}

for key in current_movies:
    print(key)

movie = input("What movie would you like the show time for?\n")

showtime = current_movies.get(movie)

if showtime == None:
    print("The requested movie is not playing.")
else: 
    print(movie, "is showing at", showtime)