def make_album(artist_name, album_title, number_of_tracks):
    D_album = artist_name + ', '+ album_title + ', ' + number_of_tracks
    return D_album.title()
while True:
    print("Give me the description of the album:")
    print("(enter 'q' to quit)")

    a_name = input("Artist name: ")
    if a_name == 'q':
        break

    a_title = input("Album title: ")
    if a_title == 'q':
        break
    N_tracks = input("number of tracks: ")
    N_tracks = int(N_tracks)
    if N_tracks == 'q':
        break
    
    description_album = make_album(a_name, a_title, N_tracks)
    print(description_album)
