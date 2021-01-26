from Nested_data import albums

while True:
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{0}: {1}".format(index+1, title))
    choice = int(input("Please select you choice(invalid number will exit the code"))
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][3]
    else:
        break
    for item, (song_number, song_title) in enumerate(songs_list):
        print("{0}: {1}".format(song_number, song_title))
    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][1]
    else:
        continue
    print("Playing {}".format(title))
    print("*" * 40)

