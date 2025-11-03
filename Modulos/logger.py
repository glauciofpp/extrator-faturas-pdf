import logging
import os
from config import LOGS_FOLDER, LOGGING_LEVEL

os.makedirs(LOGS_FOLDER, exist_ok=True)

LOG_FILE = os.path.join(LOGS_FOLDER, "geral.log")

logger = logging.getLogger("logger_geral")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s",datefmt="%d-%m-%Y %H:%M:%S")

file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
file_handler.setFormatter(formatter)
file_handler.setLevel(LOGGING_LEVEL)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(LOGGING_LEVEL)

if not logger.hasHandlers():
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)