from app.database import get_connection


class RegistrationRepository:
    def create(self, event_id: int, participant_id: int) -> dict:
        with get_connection() as connection:
            cursor = connection.execute(
                """
                INSERT INTO registrations (event_id, participant_id)
                VALUES (?, ?)
                """,
                (event_id, participant_id),
            )

            registration_id = cursor.lastrowid

            row = connection.execute(
                "SELECT * FROM registrations WHERE id = ?",
                (registration_id,),
            ).fetchone()

            return dict(row)

    def get_all(self) -> list[dict]:
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT * FROM registrations ORDER BY id"
            ).fetchall()

            return [dict(row) for row in rows]