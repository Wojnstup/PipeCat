import sqlite3
import os
import random
from logger import throw_error

def get_lists():
    connection = sqlite3.connect("data/playlists.db")
    cursor = connection.cursor()
    
    tables = []

    cursor.execute("""
        SELECT name FROM sqlite_master WHERE type='table'
    """)
    dumb_tables = cursor.fetchall()

    for touple in dumb_tables:
        tables.append(touple[0])

    connection.close()
    return tables

def create_playlist(name):

    if name in get_lists():
        throw_error("Playlist already exists!")
        return


    connection = sqlite3.connect("data/playlists.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE {name} (
            title text,
            url text
        )
    """.format(name=name))

    connection.commit()
    connection.close()

def add_song(list_name, song_title, song_url):
    connection = sqlite3.connect("data/playlists.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO {list_name} VALUES (?,?)
    """.format(list_name=list_name), (song_title, song_url))

    connection.commit()
    connection.close()

def get_list(playlist):
    connection = sqlite3.connect("data/playlists.db")
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT
                title, url
            FROM
                {playlist}
        """.format(playlist=playlist))

        content = cursor.fetchall()

        connection.close()
        return content
    except:
        throw_error("NO SUCH PLAYLIST")
        connection.close()

def play_list(list, start = -318, shuffle = False, video=False):
    if not list:
        return

    if start > 0:
        start = start - 1

    if shuffle == False:
        index = 0
        for song in list:
            if index < start:
                index = index + 1
                continue
            index = index + 1

            print("")
            print(song[0])
            print("")

            if video:
                os.system("mpv {url}".format(url=song[1]))
                return
            else:
                os.system("mpv {url} --no-video".format(url=song[1]))
    else:

        indexes = [*range(0, len(list))]
        if start >= 0:
            indexes.remove(start)

        random.shuffle(indexes)
        if start >= 0:
            indexes = [start] + indexes

        #print(indexes)

        for index in indexes:
            print("")
            print(list[index][0])
            print("")
            
            if video:
                os.system("mpv {url}".format(url=list[index][1]))
                return
            else:
                os.system("mpv {url} --no-video".format(url=list[index][1]))

def remove_song_from_list(list_name, song_name):
    connection = sqlite3.connect("data/playlists.db")
    cursor = connection.cursor()

    try:
        cursor.execute("""
            DELETE FROM '{list_name}' WHERE title = ?
        """.format(list_name = str(list_name)),  (str(song_name), ))
    except:
        throw_error("NO SUCH LIST")

    connection.commit()
    connection.close()    
