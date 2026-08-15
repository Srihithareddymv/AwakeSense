from pathlib import Path

PROJECT_NAME = "AwakeSense"

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_NAME = "awakesense.db"

DATABASE_PATH = BASE_DIR / DATABASE_NAME

HOST = "127.0.0.1"

PORT = 8000