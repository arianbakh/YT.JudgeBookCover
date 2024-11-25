import os
from pathlib import Path
from peewee import SqliteDatabase, Model, IntegerField, CharField


DATA_DIR = os.path.join(Path(__file__).parent.parent.parent, "data")
DB_PATH = os.path.join(DATA_DIR, "books.db")
DB = SqliteDatabase(DB_PATH)


class Book(Model):
    one_star = IntegerField()
    two_star = IntegerField()
    three_star = IntegerField()
    four_star = IntegerField()
    five_star = IntegerField()
    image_path = CharField()

    class Meta:
        database = DB
