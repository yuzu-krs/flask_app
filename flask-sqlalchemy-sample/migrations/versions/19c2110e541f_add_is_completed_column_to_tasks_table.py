"""Add is_completed column to tasks table

Revision ID: 19c2110e541f
Revises: 
Create Date: 2024-02-07 19:25:00.386508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19c2110e541f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_completed', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.drop_column('is_completed')

    # ### end Alembic commands ###
