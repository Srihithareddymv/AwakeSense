import sqlite3
from pathlib import Path


class DatabaseManager:

    def __init__(self):

        Path("database/sqlite").mkdir(parents=True, exist_ok=True)

        self.connection = sqlite3.connect(
            "database/sqlite/database.db"
        )

        self.cursor = self.connection.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TEXT,

            blinks INTEGER,

            yawns INTEGER,

            fatigue INTEGER,

            status TEXT

        )
        """)

        self.connection.commit()

    def save_session(
        self,
        timestamp,
        blinks,
        yawns,
        fatigue,
        status
    ):

        self.cursor.execute("""

        INSERT INTO sessions
        (timestamp,blinks,yawns,fatigue,status)

        VALUES(?,?,?,?,?)

        """, (
            timestamp,
            blinks,
            yawns,
            fatigue,
            status
        ))

        self.connection.commit()

    def close(self):

        self.connection.close()