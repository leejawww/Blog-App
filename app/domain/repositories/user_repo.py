from fastapi import Depends
from sqlalchemy.orm import Session
from app.infrastructure.models.user_models import User
from app.core.database import get_db


class UserRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    def create(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get(self, id: int, user: User):
        return self.db.get(User, user.id)

    def update(self, id: int, user: User):
        user.id = id
        self.db.merge(user)
        self.db.commit()
        return user

    def delete(self, user: User) -> None:
        self.db.delete(user)
        self.db.commit()
        self.db.flush()
