def make_album(artist_name, album_title, number_of_tracks:''):
    album ={'A_name' : artist_name, 'A_title' : album_title, 'A_traks' : number_of_tracks}
    return album
description_album = make_album('Michael Jackson', 'Thriller', '5')
print(description_album)
