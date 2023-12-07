"""Remove is_hidden.

Revision ID: 5883dd3619bf
Revises: bc9e3f681186
Create Date: 2023-11-29 11:25:49.979260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5883dd3619bf'
down_revision = 'bc9e3f681186'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('is_hidden')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_hidden', sa.BOOLEAN(), autoincrement=False, nullable=False))

    # ### end Alembic commands ###