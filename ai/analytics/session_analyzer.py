import sqlite3


class SessionAnalyzer:

    def __init__(self):

        self.connection = sqlite3.connect(
            "database/sqlite/database.db"
        )

        self.cursor = self.connection.cursor()

    def total_sessions(self):

        self.cursor.execute(
            "SELECT COUNT(*) FROM sessions"
        )

        return self.cursor.fetchone()[0]

    def average_fatigue(self):

        self.cursor.execute(
            "SELECT AVG(fatigue) FROM sessions"
        )

        result = self.cursor.fetchone()[0]

        if result is None:
            return 0

        return round(result, 2)

    def highest_fatigue(self):

        self.cursor.execute(
            "SELECT MAX(fatigue) FROM sessions"
        )

        result = self.cursor.fetchone()[0]

        if result is None:
            return 0

        return result

    def close(self):

        self.connection.close()