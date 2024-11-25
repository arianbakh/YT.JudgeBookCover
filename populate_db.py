import argparse
from judge.db import DB, Book


def populate(data_dir: str):
    DB.connect()
    DB.create_tables([Book])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=str, required=True, help="Directory of the image files")
    args = parser.parse_args()
    populate(args.data_dir)
