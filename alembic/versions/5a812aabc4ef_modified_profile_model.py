"""Modified profile model

Revision ID: 5a812aabc4ef
Revises: 362e462891c9
Create Date: 2025-01-18 21:14:16.665029+00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5a812aabc4ef'
down_revision: Union[str, None] = '362e462891c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profile', sa.Column('years_of_experience', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('profile', 'years_of_experience')
    # ### end Alembic commands ###