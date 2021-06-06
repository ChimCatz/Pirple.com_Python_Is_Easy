# My Favorite Song
# Supermarket Flowers by Ed Sheeran
"""
Supermarket Flowers is a song composed and produced by Ed Sheeran, an English singer-songwriter.
It was recorded on 2016 and released on 2018.
It is the 12th track of the Album "Divide"
"""

SupermarketFlowers = {
    "Title": "Supermarket Flowers",
    "Artist": "Ed Sheeran",
    "Album": "Divide",
    "Genre": "Pop Song",
    "YearReleased": 2018,
    "YearRecorded": 2016,
    "DurationInSeconds": 221,
    "SpotifyStreams_inMillions": 56.73,
    "Songwriters": "Ed Sheeran, Johnny McDaid, and Benjamin Levin",
    "Producers": "Ed Sheeran, Benny Blanco, and Johnny McDaid"
}

print("MY FAVORITE SONG")
view = int(input("What do you want to do? \nPress 1 to CHECK song information\nPress 2 to GUESS song information\n"))
if view == 1:
    for info in SupermarketFlowers:
        print(info, ": ", SupermarketFlowers[info])
elif view == 2:
    def guessing_game():
        while True:
            for data in SupermarketFlowers:
                keys = list(SupermarketFlowers.keys())
                print(keys)
                data = input("Which key would you like to guess?:\n")
                if data in SupermarketFlowers:
                    a = input("Guess the " + data + "?:\n")
                    if SupermarketFlowers[data] == a:
                        print("You are CORRECT!")
                        return
                    else:
                        print("You are WRONG. Try again!")

                else:
                    print("WRONG key!\n")


    guessing_game()

print("Thank you")
