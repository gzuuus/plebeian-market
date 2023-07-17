"""Simplify Nostr auth.

Revision ID: fe81d57b48b4
Revises: f16c319d7a0f
Create Date: 2023-07-17 08:11:09.746090

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fe81d57b48b4'
down_revision = 'f16c319d7a0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('nostr_auth', schema=None) as batch_op:
        batch_op.drop_index('ix_nostr_auth_key')

    op.drop_table('nostr_auth')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nostr_auth',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('verification_phrase', sa.VARCHAR(length=32), autoincrement=False, nullable=False),
    sa.Column('key', sa.VARCHAR(length=64), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='nostr_auth_pkey')
    )
    with op.batch_alter_table('nostr_auth', schema=None) as batch_op:
        batch_op.create_index('ix_nostr_auth_key', ['key'], unique=False)

    # ### end Alembic commands ###
