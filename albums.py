import sqlite3
import logger

def add_album(title, url):
    if not title or not url:
        throw_error("No title or no URL") 
        return

    connection = sqlite3.connect("data/albums.db")
    cursor = connection.cursor()


    cursor.execute("""
        INSERT INTO albums VALUES (?,?)
    """, (str(title), str(url) ))

    connection.commit()
    connection.close()

def get_albums():
    connection = sqlite3.connect("data/albums.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM albums
    """)

    albums = cursor.fetchall()

    connection.commit()
    connection.close()
    return albums
