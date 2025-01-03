"""add author and category fields

Revision ID: 823a4ad95441
Revises: 09acd1ef4a63
Create Date: 2024-12-28 14:23:38.535198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '823a4ad95441'
down_revision = '09acd1ef4a63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('category', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('category')
        batch_op.drop_column('author')

    # ### end Alembic commands ###
