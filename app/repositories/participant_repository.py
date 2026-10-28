from app.database import get_connection
from app.models.participant import Participant


class ParticipantRepository:
    def create(self, participant: Participant) -> dict:
        with get_connection() as connection:
            cursor = connection.execute(
                """
                INSERT INTO participants (name, email)
                VALUES (?, ?)
                """,
                (participant.name, participant.email),
            )

            participant_id = cursor.lastrowid

            row = connection.execute(
                "SELECT * FROM participants WHERE id = ?",
                (participant_id,),
            ).fetchone()

            return dict(row)

    def get_all(self) -> list[dict]:
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT * FROM participants ORDER BY id"
            ).fetchall()

            return [dict(row) for row in rows]