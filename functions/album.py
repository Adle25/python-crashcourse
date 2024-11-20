def make_album(artist_name, album_title, number_song=None):
    album = {
        'artist_name': artist_name,
        'album_title': album_title
    }

    if number_song:
        album['song_number'] = number_song

    return album


while True:
    print('\nHello user enter artist name and album title.')
    print(f'Enter \'q\' to exit')

    name = input('Enter artist name: ')

    if name == 'q':
        break

    title = input('Enter album title: ')

    if title == 'q':
        break

    album = make_album(name, title)

    print(album)


