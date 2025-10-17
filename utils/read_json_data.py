import json
from utils.logger import get_logger

logger = get_logger(__name__)

def read_json_file(file_path):
    logger.info("Reading json file: " + file_path)
    with open(file_path, "r") as file:
        data = json.load(file)
    logger.debug("Json file read successfully: %s", data)

    return data
    