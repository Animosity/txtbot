"""empty message

Revision ID: 8fd02b110714
Revises: 
Create Date: 2018-03-11 11:34:03.590908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fd02b110714'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('nickname', sa.String(length=32), nullable=True),
    sa.Column('discord_id', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('avatar_uri', sa.String(length=256), nullable=True),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_authors_discord_id'), 'authors', ['discord_id'], unique=True)
    op.create_index(op.f('ix_authors_email'), 'authors', ['email'], unique=True)
    op.create_index(op.f('ix_authors_nickname'), 'authors', ['nickname'], unique=True)
    op.create_table('curators',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('nickname', sa.String(length=32), nullable=True),
    sa.Column('discord_id', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('avatar_uri', sa.String(length=256), nullable=True),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_curators_discord_id'), 'curators', ['discord_id'], unique=True)
    op.create_index(op.f('ix_curators_email'), 'curators', ['email'], unique=True)
    op.create_index(op.f('ix_curators_nickname'), 'curators', ['nickname'], unique=True)
    op.create_table('articles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('curator_id', sa.Integer(), nullable=True),
    sa.Column('discord_msg_id', sa.String(length=128), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(length=256), nullable=True),
    sa.Column('content', sa.String(length=1024), nullable=True),
    sa.Column('attachment', sa.String(length=512), nullable=True),
    sa.Column('visible', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ),
    sa.ForeignKeyConstraint(['curator_id'], ['curators.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_articles_discord_msg_id'), 'articles', ['discord_msg_id'], unique=True)
    op.create_index(op.f('ix_articles_timestamp'), 'articles', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_articles_timestamp'), table_name='articles')
    op.drop_index(op.f('ix_articles_discord_msg_id'), table_name='articles')
    op.drop_table('articles')
    op.drop_index(op.f('ix_curators_nickname'), table_name='curators')
    op.drop_index(op.f('ix_curators_email'), table_name='curators')
    op.drop_index(op.f('ix_curators_discord_id'), table_name='curators')
    op.drop_table('curators')
    op.drop_index(op.f('ix_authors_nickname'), table_name='authors')
    op.drop_index(op.f('ix_authors_email'), table_name='authors')
    op.drop_index(op.f('ix_authors_discord_id'), table_name='authors')
    op.drop_table('authors')
    # ### end Alembic commands ###