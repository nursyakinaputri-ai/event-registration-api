from app.database import get_connection
from app.models.event import Event


class EventRepository:
    def create(self, event: Event) -> dict:
        with get_connection() as connection:
            cursor = connection.execute(
                """
                INSERT INTO events (name, description, location, date, capacity)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    event.name,
                    event.description,
                    event.location,
                    event.date,
                    event.capacity,
                ),
            )

            event_id = cursor.lastrowid

            row = connection.execute(
                "SELECT * FROM events WHERE id = ?",
                (event_id,),
            ).fetchone()

            return dict(row)

    def get_all(self) -> list[dict]:
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT * FROM events ORDER BY id"
            ).fetchall()

            return [dict(row) for row in rows]