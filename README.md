# Setup

1. `conda env create --file conda.yaml --solver libmamba`
2. `conda activate yt-book`
3. `export PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring`
4. `poetry install`

# Usage

1. `python populate_db.py --data-dir data/dataset_v3`
2. `python detect_objects.py --model models/yolo11x.pt --bs 128`
