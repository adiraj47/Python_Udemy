name = "Welcome to my nightmare", "Alice Cooper", 1975
bad = "bad company", "bad company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
mettalica = "Ride the lighting", "Mettalica", 1984
print(mettalica)
mettalica2 = list(mettalica)
print(mettalica2)
title, writer, year = mettalica
print(title, writer, year)
alubums = [("Welcome to my nightmare", "Alice Cooper", 1975),
          ("bad company", "bad company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the lighting", "Mettalica", 1984),
          ]
print(len(alubums))
for alubum in alubums:
    name, artist, year = alubum
    print("Artist {0} Writer: {1} Year: {2}"
          .format(name, artist, year))