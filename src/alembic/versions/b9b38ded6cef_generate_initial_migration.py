"""generate initial migration

Revision ID: b9b38ded6cef
Revises: 179f5b7a7f97
Create Date: 2023-09-19 15:39:46.227207

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b9b38ded6cef"
down_revision: Union[str, None] = "179f5b7a7f97"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###