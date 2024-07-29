"""Create user table

Revision ID: bee8b5fe3222
Revises:
Create Date: 2024-07-29 12:16:21.885134

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "bee8b5fe3222"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "blog",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String(20)),
        sa.Column("content", sa.String(1000)),
        sa.Column("author_id", sa.Integer),
        sa.Column("author_name", sa.String(50)),
        sa.Column("published_on", sa.DateTime()),
    )


def downgrade() -> None:
    op.drop_table("blog")
