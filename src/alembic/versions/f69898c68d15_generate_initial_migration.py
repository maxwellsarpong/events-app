"""generate initial migration

Revision ID: f69898c68d15
Revises: 7a72b9c2a55c
Create Date: 2023-09-26 18:27:20.393123

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f69898c68d15"
down_revision: Union[str, None] = "7a72b9c2a55c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "verification",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("certificate", sa.String(), nullable=False),
        sa.Column("verification_code", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("skill_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["skill_id"],
            ["skill.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("certificate"),
        sa.UniqueConstraint("verification_code"),
    )
    op.create_index(op.f("ix_verification_id"), "verification", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_verification_id"), table_name="verification")
    op.drop_table("verification")
    # ### end Alembic commands ###
