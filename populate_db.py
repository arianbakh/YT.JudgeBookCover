import argparse
from judge.db import DB
import os
from tqdm import tqdm


def populate(data_dir: str):
    for file_name in tqdm(os.listdir(data_dir)):
        if file_name.endswith(".jpg"):
            id = int(file_name.split("_")[0])
            star1, star2, star3, star4, star5 = [
                int(item) for item in file_name.split("_")[1].split(".")[0].split("-")
            ]
            image_path = os.path.join(data_dir, file_name)
            DB.insert({
                "id": id,
                "star1": star1,
                "star2": star2,
                "star3": star3,
                "star4": star4,
                "star5": star5,
                "image_path": image_path
            })


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=str, required=True, help="Directory of the image files")
    args = parser.parse_args()
    populate(args.data_dir)
