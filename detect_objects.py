import argparse
from judge.db import DB
import logging
import math
from tinydb import Query
from tqdm import tqdm
from typing import List
import ultralytics
from ultralytics import YOLO


logging.getLogger("ultralytics").setLevel(logging.ERROR)


def get_model(model_path: str):
    model = YOLO(model_path)
    model.eval()
    model.cuda()
    return model


def get_objects_from_result(result: ultralytics.engine.results.Results, class_names: dict):
    objects = set()
    for box in result.boxes:
        class_index = int(box.cls)
        class_name = class_names[class_index]
        objects.add(class_name)
    return list(objects)


def get_image_list_objects(model: ultralytics.models.yolo.model.YOLO, image_paths: List[str], batch_size: int):
    objects_list = []
    num_batches = math.ceil(len(image_paths) / batch_size)
    for batch_index in tqdm(range(num_batches), desc="Detecting objects"):
        batch = image_paths[batch_index * batch_size:(batch_index + 1) * batch_size]
        results = model(batch, stream=True)
        for result in results:
            objects_list.append(get_objects_from_result(result, model.names))
    return objects_list


def detect_objects(model: ultralytics.models.yolo.model.YOLO, batch_size: int):
    image_paths = []
    ids = []
    for item in DB:
        image_paths.append(item["image_path"])
        ids.append(item["id"])
    objects_list = get_image_list_objects(model, image_paths, batch_size)
    book = Query()
    for i in tqdm(range(len(ids)), desc="Updating DB"):
        DB.update({"objects": objects_list[i]}, book.id == ids[i])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, required=True, help="Path of the model weights")
    parser.add_argument("--bs", type=int, required=True, help="Batch size")
    args = parser.parse_args()
    model = get_model(args.model)
    detect_objects(model, args.bs)
