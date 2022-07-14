"""Add verification tweet ID.

Revision ID: 7b9b9d83c135
Revises: 0b933fdb55c0
Create Date: 2022-06-28 13:20:03.030794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b9b9d83c135'
down_revision = '0b933fdb55c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('twitter_username_verification_tweet_id', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'twitter_username_verification_tweet_id')
    # ### end Alembic commands ###