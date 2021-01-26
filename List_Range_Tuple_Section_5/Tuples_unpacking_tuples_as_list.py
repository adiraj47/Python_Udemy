# imelda = "More mayhem", "imelda",2011,(
#     (1,"Pulling the rug"),(2,"Pyshco"),(3,"Mayhem"),(4,"Kentish"))
# tittle, artist, year, tracks = imelda
# for songs in tracks:
#     track, song= songs
#     print("The track no is {} and the song name is {}".format(track, song))
#Creating a list inside a tuple
imelda = "More mayhem", "imelda",2011,(
    [(1,"Pulling the rug"),(2,"Pyshco"),(3,"Mayhem"),(4,"Kentish")])
imelda[3].append((5,"All for you"))
tittle, artist, year, tracks = imelda
tracks.append((6,"Eternity"))
for songs in tracks:
    track, song= songs
    print("The track no is {} and the song name is {}".format(track, song))

