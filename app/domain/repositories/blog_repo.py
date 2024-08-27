from sqlalchemy.orm import Session
from infrastructure.models.blog_models import Blog


class BlogRepository:
    db: Session

    def create(self, blog: Blog):
        self.db.add(blog)
        self.db.commit()
        self.db.refresh(blog)
        return blog

    def get(self, id: int, blog: Blog):
        return self.db.get(Blog, blog.id)

    def update(self, id: int, blog: Blog):
        blog.id = id
        self.db.merge(blog)
        self.db.commit()
        return blog

    def delete(self, blog: Blog):
        self.db.delete(blog)
        self.db.commit()
        self.db.flush()
