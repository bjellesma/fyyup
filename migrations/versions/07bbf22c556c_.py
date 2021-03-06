"""empty message

Revision ID: 07bbf22c556c
Revises: cad6ac6e3a70
Create Date: 2020-06-14 02:13:24.872701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07bbf22c556c'
down_revision = 'cad6ac6e3a70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist_show', sa.Column('artist_id', sa.Integer(), nullable=False))
    op.drop_constraint('artist_show_venue_id_fkey', 'artist_show', type_='foreignkey')
    op.create_foreign_key(None, 'artist_show', 'artist', ['artist_id'], ['id'])
    op.drop_column('artist_show', 'venue_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist_show', sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'artist_show', type_='foreignkey')
    op.create_foreign_key('artist_show_venue_id_fkey', 'artist_show', 'venue', ['venue_id'], ['id'])
    op.drop_column('artist_show', 'artist_id')
    # ### end Alembic commands ###
