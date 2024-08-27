from app.api.schemas.user_schemas import UserCreate
from app.infrastructure.models.user_models import User
from app.domain.repositories.user_repo import UserRepository


class UserControl:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create(self, user_create: UserCreate):
        return self.user_repo.create(
            User(
                username=user_create.username,
                id=user_create.id,
                email=user_create.email,
                password=user_create.password,
            )
        )

    def get(self, id: int, user_create: UserCreate):
        return self.user_repo.get(
            id,
            User(
                username=user_create.username,
                id=user_create.id,
                email=user_create.email,
                password=user_create.password,
            ),
        )

    def update(self, id: int, user_create: UserCreate):
        return self.user_repo.update(
            id,
            User(
                username=user_create.username,
                id=user_create.id,
                email=user_create.email,
                password=user_create.password,
            ),
        )

    def delete(self, id: int) -> None:
        return self.user_repo.delete(id)  # type: ignore
