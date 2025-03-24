from typing import Optional
from core.models.users import User
from core.utils.database import Database
from datetime import datetime
import uuid

db = Database()


class UserRepository:

    @staticmethod
    def create(name: str, status: str = "active") -> User:
        user_id = str(uuid.uuid4())
        now = datetime.utcnow()

        query = """
            INSERT INTO users (id, name, status, created_timestamp, updated_timestamp)
            VALUES (%s, %s, %s, %s, %s)
        """
        params = (user_id, name, status, now, now)
        db.run_query(query, params)

        return User(
            id=user_id,
            name=name,
            status=status,
            created_timestamp=now,
            updated_timestamp=now
        )

    @staticmethod
    def get(user_id: str) -> Optional[User]:
        query = "SELECT * FROM users WHERE id = %s"
        rows = db.run_query(query, (user_id,))
        return User(**rows[0]) if rows else None

    @staticmethod
    def update(user_id: str, updates: dict) -> Optional[User]:
        if not updates:
            return None

        fields = ", ".join([f"{k} = %s" for k in updates])
        values = list(updates.values())
        values.append(datetime.utcnow())  # for updated_timestamp
        values.append(user_id)

        query = f"""
            UPDATE users SET {fields}, updated_timestamp = %s
            WHERE id = %s
        """
        db.run_query(query, tuple(values))
        return UserRepository.get(user_id)

    @staticmethod
    def delete(user_id: str) -> bool:
        query = "DELETE FROM users WHERE id = %s"
        db.run_query(query, (user_id,))
        return True