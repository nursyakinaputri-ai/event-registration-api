from contextlib import contextmanager
import os
import sqlite3
from pathlib import Path


DATABASE_PATH = Path(
    os.environ.get(
        "DATABASE_PATH",
        str(Path(__file__).resolve().parent.parent / "event_registration.db"),
    )
)



@contextmanager
def get_connection():
    database_path = os.environ.get("DATABASE_PATH", str(DATABASE_PATH))
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row

    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def initialize_database():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL DEFAULT '',
                location TEXT NOT NULL,
                date TEXT NOT NULL,
                capacity INTEGER NOT NULL CHECK (capacity > 0)
            )
            """
        )

        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS participants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
            """
        )

        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS registrations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_id INTEGER NOT NULL,
                participant_id INTEGER NOT NULL,
                FOREIGN KEY (event_id) REFERENCES events(id),
                FOREIGN KEY (participant_id) REFERENCES participants(id),
                UNIQUE (event_id, participant_id)
            )
            """
        )


initialize_database()
