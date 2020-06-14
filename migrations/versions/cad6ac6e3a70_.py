"""empty message

Revision ID: cad6ac6e3a70
Revises: a1728005f9bd
Create Date: 2020-06-13 22:05:01.083111

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'cad6ac6e3a70'
down_revision = 'a1728005f9bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('website', sa.String(length=500), nullable=True),
    sa.Column('facebook_link', sa.String(length=500), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('seeking_venue', sa.Boolean(), nullable=False),
    sa.Column('seeking_description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('genre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('venue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(length=120), nullable=False),
    sa.Column('city', sa.String(length=120), nullable=False),
    sa.Column('state', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('website', sa.String(length=500), nullable=True),
    sa.Column('facebook_link', sa.String(length=500), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('seeking_talent', sa.Boolean(), nullable=False),
    sa.Column('seeking_description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('artist_genre_artist_id_fkey', 'artist_genre', type_='foreignkey')
    op.drop_constraint('artist_genre_genre_id_fkey', 'artist_genre', type_='foreignkey')
    op.create_foreign_key(None, 'artist_genre', 'genre', ['genre_id'], ['id'])
    op.create_foreign_key(None, 'artist_genre', 'artist', ['artist_id'], ['id'])
    op.drop_constraint('artist_show_venue_id_fkey', 'artist_show', type_='foreignkey')
    op.drop_constraint('artist_show_show_id_fkey', 'artist_show', type_='foreignkey')
    op.create_foreign_key(None, 'artist_show', 'show', ['show_id'], ['id'])
    op.create_foreign_key(None, 'artist_show', 'venue', ['venue_id'], ['id'])
    op.drop_constraint('venue_genre_genre_id_fkey', 'venue_genre', type_='foreignkey')
    op.drop_constraint('venue_genre_venue_id_fkey', 'venue_genre', type_='foreignkey')
    op.create_foreign_key(None, 'venue_genre', 'genre', ['genre_id'], ['id'])
    op.create_foreign_key(None, 'venue_genre', 'venue', ['venue_id'], ['id'])
    op.drop_constraint('venue_show_venue_id_fkey', 'venue_show', type_='foreignkey')
    op.drop_constraint('venue_show_show_id_fkey', 'venue_show', type_='foreignkey')
    op.create_foreign_key(None, 'venue_show', 'show', ['show_id'], ['id'])
    op.create_foreign_key(None, 'venue_show', 'venue', ['venue_id'], ['id'])
    op.drop_table('Artist')
    op.drop_table('Genre')
    op.drop_table('Show')
    op.drop_table('Venue')
    
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'venue_show', type_='foreignkey')
    op.drop_constraint(None, 'venue_show', type_='foreignkey')
    op.create_foreign_key('venue_show_show_id_fkey', 'venue_show', 'Show', ['show_id'], ['id'])
    op.create_foreign_key('venue_show_venue_id_fkey', 'venue_show', 'Venue', ['venue_id'], ['id'])
    op.drop_constraint(None, 'venue_genre', type_='foreignkey')
    op.drop_constraint(None, 'venue_genre', type_='foreignkey')
    op.create_foreign_key('venue_genre_venue_id_fkey', 'venue_genre', 'Venue', ['venue_id'], ['id'])
    op.create_foreign_key('venue_genre_genre_id_fkey', 'venue_genre', 'Genre', ['genre_id'], ['id'])
    op.drop_constraint(None, 'artist_show', type_='foreignkey')
    op.drop_constraint(None, 'artist_show', type_='foreignkey')
    op.create_foreign_key('artist_show_show_id_fkey', 'artist_show', 'Show', ['show_id'], ['id'])
    op.create_foreign_key('artist_show_venue_id_fkey', 'artist_show', 'Venue', ['venue_id'], ['id'])
    op.drop_constraint(None, 'artist_genre', type_='foreignkey')
    op.drop_constraint(None, 'artist_genre', type_='foreignkey')
    op.create_foreign_key('artist_genre_genre_id_fkey', 'artist_genre', 'Genre', ['genre_id'], ['id'])
    op.create_foreign_key('artist_genre_artist_id_fkey', 'artist_genre', 'Artist', ['artist_id'], ['id'])
    op.create_table('Venue',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Venue_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('address', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('state', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('phone', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('website', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('facebook_link', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('image_link', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('seeking_talent', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('seeking_description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Venue_pkey')
    )
    op.create_table('Show',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Show_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('start_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='Show_pkey')
    )
    op.create_table('Genre',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Genre_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Genre_pkey')
    )
    op.create_table('Artist',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Artist_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('state', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('phone', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('website', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('facebook_link', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('image_link', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('seeking_venue', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('seeking_description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Artist_pkey')
    )
    op.drop_table('venue')
    op.drop_table('show')
    op.drop_table('genre')
    op.drop_table('artist')
    # ### end Alembic commands ###
