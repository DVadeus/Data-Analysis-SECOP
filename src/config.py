import os

DATASET_ID = "jbjy-vk9h"
URL = f"https://www.datos.gov.co/resource/{DATASET_ID}.json"
ID_TOKEN = os.getenv("ID_TOKEN")

LIMIT = 50000
START_YEAR = 2018
END_YEAR = 2025

OUTPUT_PATH = "data/raw"