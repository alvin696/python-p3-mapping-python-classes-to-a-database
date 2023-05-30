from config import CONN, CURSOR

import sqlite3

DB_NAME = 'music.db'
TABLE_NAME = 'songs'

class Song:
    def __init__(self, name, album, id=None):
        self.id = id
        self.name = name
        self.album = album

    def save(self):
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO {TABLE_NAME} (name, album) VALUES (?, ?)", (self.name, self.album))
            self.id = cursor.lastrowid
            conn.commit()

    @classmethod
    def create(cls, name, album):
        song = cls(name, album)
        song.save()
        return song

    @classmethod
    def create_table(cls):
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, album TEXT)")
            conn.commit()
