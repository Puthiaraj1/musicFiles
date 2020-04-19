import os
import fnmatch


def find_albums(root, artist_name):
    for path, directories, files in os.walk(root):
        #for artist in fnmatch.filter(directories, artist_name):
        for artist in fnmatch.filter(directories, artist_name):
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_song(albums):
    for album in albums:
        for song in os.listdir(album[0]):
            yield song


def find_music(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            absolute_path = os.path.abspath(path)
            yield os.path.join(absolute_path, file)

album_list = find_albums("music", "U2")
song_list = find_song(album_list)

for m in find_music('music', 'emp3'):
    print(m)

# for s in song_list:
#     print(s)