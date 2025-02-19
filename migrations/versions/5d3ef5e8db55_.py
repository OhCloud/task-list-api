"""empty message

Revision ID: 5d3ef5e8db55
Revises: 29b91b61ddcf
Create Date: 2021-06-15 12:39:42.033091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d3ef5e8db55'
down_revision = '29b91b61ddcf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('goal_id', sa.Integer(), nullable=True))
    op.add_column('task', sa.Column('is_complete', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'is_complete')
    op.drop_column('task', 'goal_id')
    # ### end Alembic commands ###
