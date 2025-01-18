"""create admins table

Revision ID: e6bcbd2b0769
Revises: ab097eacba6c
Create Date: 2025-01-18 13:21:24.475889+00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e6bcbd2b0769'
down_revision: Union[str, None] = 'ab097eacba6c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
