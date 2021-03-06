"""add can_comment for Post model

Revision ID: d6072898d8fa
Revises: 9e27b36c0937
Create Date: 2021-10-20 20:23:22.587853

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6072898d8fa'
down_revision = '9e27b36c0937'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('can_comment', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'can_comment')
    # ### end Alembic commands ###
