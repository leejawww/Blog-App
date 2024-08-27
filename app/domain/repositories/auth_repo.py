from sqlalchemy.orm import Session
from infrastructure.models.auth_models import AuthUser


class AuthRepository:
    db: Session

    def create(self, blog: AuthUser):
        self.db.add(blog)
        self.db.commit()
        self.db.refresh(blog)
        return blog
