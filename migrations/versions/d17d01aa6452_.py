"""empty message

Revision ID: d17d01aa6452
Revises: 695505648be4
Create Date: 2023-08-26 00:04:39.936562

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd17d01aa6452'
down_revision = '695505648be4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('charges', schema=None) as batch_op:
        batch_op.drop_column('latefee')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('charges', schema=None) as batch_op:
        batch_op.add_column(sa.Column('latefee', sa.INTEGER(), nullable=True))

    # ### end Alembic commands ###