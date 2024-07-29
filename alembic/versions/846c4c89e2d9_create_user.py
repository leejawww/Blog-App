"""Create user

Revision ID: 846c4c89e2d9
Revises: bee8b5fe3222
Create Date: 2024-07-29 13:03:28.152250

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "846c4c89e2d9"
down_revision: Union[str, None] = "bee8b5fe3222"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.String(50)),
        sa.Column("email", sa.String(50)),
        sa.Column("password", sa.String(20)),
    )


def downgrade() -> None:
    pass
