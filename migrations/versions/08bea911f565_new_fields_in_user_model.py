"""new fields in user model

Revision ID: 08bea911f565
Revises: cf1720b49473
Create Date: 2020-04-17 16:03:56.518182

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08bea911f565'
down_revision = 'cf1720b49473'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
