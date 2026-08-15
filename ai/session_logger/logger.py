from datetime import datetime
import json
from pathlib import Path


class SessionLogger:

    def __init__(self):

        self.log_file = Path("database/logs/session_log.json")

        if not self.log_file.exists():
            self.log_file.parent.mkdir(parents=True, exist_ok=True)
            self.log_file.write_text("[]")

    def save(self, blink_count, yawn_count, fatigue, status):

        try:
            data = json.loads(self.log_file.read_text())

        except Exception:
            data = []

        data.append(
            {
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "blinks": blink_count,
                "yawns": yawn_count,
                "fatigue": fatigue,
                "status": status,
            }
        )

        self.log_file.write_text(json.dumps(data, indent=4))