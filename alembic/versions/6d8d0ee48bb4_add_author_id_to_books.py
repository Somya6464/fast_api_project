"""add author_id to books

Revision ID: 6d8d0ee48bb4
Revises: 
Create Date: 2026-07-08 01:29:36.466940

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6d8d0ee48bb4'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('books', sa.Column('author_id', sa.Integer(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    pass
