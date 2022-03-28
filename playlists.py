import sqlite3
import os
import random
import requests
from random import randint
from youtubesearchpython import Video, ResultMode, Hashtag, VideosSearch
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

def extract_tags_from_list(list_name):
    connection = sqlite3.connect("data/playlists.db")
    cursor = connection.cursor()

    cursor.execute(""" 
        SELECT
            url
        FROM
            {playlist}
    """.format(playlist = list_name))

    urls = cursor.fetchall()
    tags = [] 

    for url in urls:
        try:
            for tag in  Video.getInfo(url[0], mode=ResultMode.json)["keywords"]:
                tags.append(tag)
        except:
            continue
       

    connection.close()
    return tags

def get_song_with_tags(tags):
    tag_num = 3

    tags_index_to_use = []
    search_term = ""

    for i in range(tag_num):
        while True:
            new_index = randint(0, len(tags) - 1)
            if not new_index in tags_index_to_use:
                tags_index_to_use.append(new_index)
                search_term = search_term + str(tags[new_index])
                break

    
    try:
        result = VideosSearch(query=search_term, limit=1).result()["result"][0]
    except:
        return False
    return (result["title"], result["link"])



def get_all_mixes():
    connection = sqlite3.connect("data/mix.db")
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

def generate_daily_mix(list_name):
    connection = sqlite3.connect("data/mix.db")
    cursor = connection.cursor()

    entries = []

    for i in range(0,10):
        while True:
            entry = get_song_with_tags(extract_tags_from_list(list_name))
            if entry:
                entries.append(entry)
                break
    
    if not list_name in get_all_mixes():
        cursor.execute("""
            CREATE TABLE {name} (
                title text,
                url text
            )
        """.format(name=list_name))
    else:
        cursor.execute("""
            DELETE FROM {name}
        """.format(name=list_name))
    

    cursor.executemany("""
        INSERT INTO {name} VALUES (?,?)
    """.format(name=list_name), entries)


    connection.commit()
    connection.close()

def get_mix(mix):
    connection = sqlite3.connect("data/mix.db")
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT
                title, url
            FROM
                {playlist}
        """.format(playlist=mix))

        content = cursor.fetchall()

        connection.close()
        return content
    except:
        throw_error("NO SUCH MIX")
        connection.close()

