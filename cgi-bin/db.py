import sqlite3
from typing import List, Callable


def sqlite_connection(func: Callable):
    """Обёртка для подключения к БД"""
    def wrapper(*args, **kwargs):
        with sqlite3.connect('db.db') as con:
            kwargs['con'] = con
            con.text_factory = lambda x: x.decode('utf-8')
            res = func(*args, **kwargs)
            con.commit()
            return res
    return wrapper


@sqlite_connection
def init_db(con: sqlite3.Connection):
    """Инициализация БД"""
    cur = con.cursor()
    """Создаём таблицу с id, названием страны"""
    cur.execute("""
        CREATE TABLE IF NOT EXISTS COUNTRIES (
            COUNTRY_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            COUNTRY_NAME TEXT
        );""")
    """Создаём таблицу с id, названием, длиной песни,  исполнителем, альбомом"""
    cur.execute("""
        CREATE TABLE IF NOT EXISTS ARTISTS (
            ARTIST_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            ARTIST_NAME TEXT,
            COUNTRY_ID INTEGER,
            FOREIGN KEY (COUNTRY_ID) REFERENCES COUNTRIES(COUNTRY_ID)
        );""")
    """Создаём таблицу с id, названием альбома, описанием альбома, количеством песен в альбоме, альбома, исполнителем"""
    cur.execute("""
            CREATE TABLE IF NOT EXISTS ALBUMS (
                ALBUM_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                ALBUM_NAME TEXT,
                ALBUM_DESCRIPTION TEXT,
                NUMBER_OF_SONGS INTEGER,
                ARTIST_ID INTEGER,
                FOREIGN KEY (ARTIST_ID) REFERENCES ARTISTS(ARTIST_ID)
            );""")
    """Создаём таблицу с id, названием песни, длиной песни,  исполнителем, альбомом"""
    cur.execute("""
        CREATE TABLE IF NOT EXISTS SONGS (
            SONG_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            SONG_NAME TEXT,
            SONG_LENGTH INTEGER,
            ARTIST_ID INTEGER,
            ALBUM_ID INTEGER,
            FOREIGN KEY (ARTIST_ID) REFERENCES ARTISTS(ARTIST_ID),
            FOREIGN KEY (ALBUM_ID) REFERENCES ALBUMS(ALBUM_ID)
        );""")
    cur.execute("INSERT INTO COUNTRIES (COUNTRY_NAME) VALUES ('Россия');")
    cur.execute("INSERT INTO COUNTRIES (COUNTRY_NAME) VALUES ('Франция');")
    cur.execute("INSERT INTO COUNTRIES (COUNTRY_NAME) VALUES ('Испания');")
    cur.execute("INSERT INTO COUNTRIES (COUNTRY_NAME) VALUES ('Италия');")
    cur.execute("INSERT INTO COUNTRIES (COUNTRY_NAME) VALUES ('Англия');")


@sqlite_connection
def get_all_songs_normalized(con: sqlite3.Connection) -> List:
    cur = con.cursor()
    cur.execute('''
        SELECT S.SONG_ID, S.SONG_NAME, S.SONG_LENGTH, A.ARTIST_NAME, L.ALBUM_NAME  FROM SONGS S
        LEFT OUTER JOIN ARTISTS A ON S.ARTIST_ID = A.ARTIST_ID
        LEFT OUTER JOIN ALBUMS L ON S.ALBUM_ID = L.ALBUM_ID
    ;''')
    return cur.fetchall()


@sqlite_connection
def get_all_countries_normalized(con: sqlite3.Connection) -> List:
    cur = con.cursor()
    cur.execute('''
            SELECT COUNTRY_NAME FROM COUNTRIES;
        ''')
    return cur.fetchall()


@sqlite_connection
def get_all_countries(con: sqlite3.Connection) -> List:
    cur = con.cursor()
    cur.execute('''
            SELECT * FROM COUNTRIES;
        ''')
    return cur.fetchall()


@sqlite_connection
def get_all_albums_normalized(con: sqlite3.Connection) -> List:
    cur = con.cursor()
    cur.execute('''
        SELECT L.ALBUM_NAME, A.ARTIST_NAME, L.ALBUM_DESCRIPTION, L.NUMBER_OF_SONGS  FROM ALBUMS L
        LEFT OUTER JOIN ARTISTS A ON L.ARTIST_ID = A.ARTIST_ID
    ;''')
    return cur.fetchall()


@sqlite_connection
def get_all_albums(con: sqlite3.Connection) -> List:
    cur = con.cursor()
    cur.execute('''
        SELECT *  FROM ALBUMS
    ;''')
    return cur.fetchall()


@sqlite_connection
def get_all_artists_normalized(con: sqlite3.Connection) -> List:
    cur = con.cursor()
    cur.execute('''
                SELECT A.ARTIST_NAME, C.COUNTRY_NAME FROM ARTISTS A
                LEFT OUTER JOIN COUNTRIES C ON A.COUNTRY_ID = C.COUNTRY_ID;
            ''')
    return cur.fetchall()


@sqlite_connection
def get_all_artists(con: sqlite3.Connection) -> List:
    cur = con.cursor()
    cur.execute('''
                SELECT * FROM ARTISTS;
            ''')
    return cur.fetchall()


@sqlite_connection
def add_artist(con: sqlite3.Connection, name: str, country_id: int):
    cur = con.cursor()
    cur.execute('''
        INSERT INTO ARTISTS (ARTIST_NAME, COUNTRY_ID) VALUES (?, ?);
    ''', (name, country_id))


@sqlite_connection
def add_country(con: sqlite3.Connection, name: str):
    cur = con.cursor()
    cur.execute('''
        INSERT INTO COUNTRIES (COUNTRY_NAME) VALUES (?);
    ''', (name,))


@sqlite_connection
def add_song(con: sqlite3.Connection, name: str, song_length: int, artist_id: int, album_id: int):
    cur = con.cursor()
    cur.execute('''
        INSERT INTO SONGS (SONG_NAME, SONG_LENGTH, ARTIST_ID, ALBUM_ID) VALUES (?, ?, ?, ?);
    ''', (name, song_length, artist_id, album_id))


@sqlite_connection
def add_album(con: sqlite3.Connection, name: str, descr: str, number_of_songs: int, artist_id: int):
    cur = con.cursor()
    cur.execute('''
        INSERT INTO ALBUMS (ALBUM_NAME, ALBUM_DESCRIPTION, NUMBER_OF_SONGS, ARTIST_ID) VALUES (?, ?, ?, ?);
    ''', (name, descr, number_of_songs, artist_id))


if __name__ == '__main__':
    init_db()
