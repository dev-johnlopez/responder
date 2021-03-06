"""empty message

Revision ID: 08fd1a9e89af
Revises: d14b04dc638f
Create Date: 2019-05-04 11:51:36.109660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08fd1a9e89af'
down_revision = 'd14b04dc638f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('account', sa.Column('name', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('account', 'name')
    # ### end Alembic commands ###
