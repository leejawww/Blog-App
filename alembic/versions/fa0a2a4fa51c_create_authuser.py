"""Create auth-user

Revision ID: fa0a2a4fa51c
Revises: 846c4c89e2d9
Create Date: 2024-07-29 14:27:08.579410

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "fa0a2a4fa51c"
down_revision: Union[str, None] = "846c4c89e2d9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "authuser",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String),
        sa.Column("password", sa.String),
    )


def downgrade() -> None:
    pass
