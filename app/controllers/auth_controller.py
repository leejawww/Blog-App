from app.api.schemas.auth_schemas import AuthUserCreate
from app.infrastructure.models.auth_models import AuthUser
from app.domain.repositories.auth_repo import AuthRepository


class AuthControl:
    def __init__(self, auth_repo: AuthRepository):
        self.auth_repo = auth_repo

    def create(self, auth_create: AuthUserCreate):
        return self.auth_repo.create(
            AuthUser(
                id=auth_create.id,
                email=auth_create.email,
                password=auth_create.password,
            )
        )
