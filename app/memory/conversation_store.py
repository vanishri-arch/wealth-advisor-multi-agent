
"""Small SQLite store for session messages and advisor summaries."""

import json
import sqlite3
from contextlib import closing
from pathlib import Path

from app.models.schemas import AdvisorSummary


class ConversationStore:
    def __init__(self, db_path: str = "wealth_advisor_memory.db"):
        self.db_path = str(db_path)
        Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)

        with closing(sqlite3.connect(self.db_path)) as connection:
            with connection:
                connection.execute(
                    """CREATE TABLE IF NOT EXISTS messages (
                        id INTEGER PRIMARY KEY,
                        session_id TEXT NOT NULL,
                        customer_id TEXT,
                        role TEXT NOT NULL,
                        content TEXT NOT NULL,
                        created_at TEXT DEFAULT CURRENT_TIMESTAMP
                    )"""
                )
                connection.execute(
                    """CREATE TABLE IF NOT EXISTS summaries (
                        id INTEGER PRIMARY KEY,
                        customer_id TEXT NOT NULL,
                        created_at TEXT NOT NULL,
                        summary_json TEXT NOT NULL,
                        human_signoff INTEGER NOT NULL DEFAULT 0
                    )"""
                )

    def record_message(
        self, session_id: str, customer_id: str, role: str, content: str
    ) -> None:
        with closing(sqlite3.connect(self.db_path)) as connection:
            with connection:
                connection.execute(
                    """INSERT INTO messages
                       (session_id, customer_id, role, content)
                       VALUES (?, ?, ?, ?)""",
                    (session_id, customer_id, role, content),
                )

    def save_summary(self, summary: AdvisorSummary) -> None:
        with closing(sqlite3.connect(self.db_path)) as connection:
            with connection:
                connection.execute(
                    """INSERT INTO summaries
                       (customer_id, created_at, summary_json, human_signoff)
                       VALUES (?, ?, ?, ?)""",
                    (
                        summary.customer_id,
                        summary.timestamp,
                        json.dumps(summary.to_dict()),
                        int(summary.human_signoff_completed),
                    ),
                )

    def get_history(self, customer_id: str) -> list[dict]:
        with closing(sqlite3.connect(self.db_path)) as connection:
            with connection:
                rows = connection.execute(
                    """SELECT summary_json FROM summaries
                       WHERE customer_id = ? ORDER BY id DESC""",
                    (customer_id,),
                ).fetchall()

        return [json.loads(row[0]) for row in rows]
