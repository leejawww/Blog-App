from app.api.schemas.blog_schemas import BlogCreate
from app.infrastructure.models.blog_models import Blog
from app.domain.repositories.blog_repo import BlogRepository


class BlogControl:
    def __init__(self, blog_repo: BlogRepository):
        self.blog_repo = blog_repo

    def create(self, blog_create: BlogCreate):
        return self.blog_repo.create(
            Blog(
                id=blog_create.id,
                title=blog_create.title,
                content=blog_create.content,
                author_id=blog_create.author_id,
                author_name=blog_create.author_name,
                published_on=blog_create.published_on,
            )
        )

    def get(self, id: int, blog_create: BlogCreate):
        return self.blog_repo.get(
            id,
            Blog(
                id=blog_create.id,
                title=blog_create.title,
                content=blog_create.content,
                author_id=blog_create.author_id,
                author_name=blog_create.author_name,
                published_on=blog_create.published_on,
            ),
        )

    def update(self, id: int, blog_create: BlogCreate):
        return self.blog_repo.update(
            id,
            Blog(
                id=blog_create.id,
                title=blog_create.title,
                content=blog_create.content,
                author_id=blog_create.author_id,
                author_name=blog_create.author_name,
                published_on=blog_create.published_on,
            ),
        )

    def delete(self, id: int) -> None:
        return self.blog_repo.delete(id)  # type: ignore
