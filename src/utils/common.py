import yaml
import sys
from src.exception import CustomException
from src.logger import logging

def read_yaml(file_path: str) -> dict:
    """
    Reads a YAML file and returns its contents as a dictionary.
    """
    try:
        logging.info(f"Reading configuration from: {file_path}")
        with open(file_path, 'r') as f:
            content = yaml.safe_load(f)
            logging.info("YAML file loaded successfully.")
            return content
    except Exception as e:
        raise CustomException(e, sys)