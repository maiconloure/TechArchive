"""Initial migration.

Revision ID: c0658d261496
Revises: 
Create Date: 2021-01-14 00:12:54.526212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0658d261496'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.Column('password', sa.String(length=1024), nullable=False),
    sa.Column('user_type', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('subtitle', sa.String(length=500), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('upvotes', sa.Integer(), nullable=True),
    sa.Column('downvotes', sa.Integer(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.Column('approved', sa.Boolean(), nullable=True),
    sa.Column('author', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('content'),
    sa.UniqueConstraint('title')
    )
    op.create_table('news_category',
    sa.Column('news_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['news_id'], ['news.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('news_category')
    op.drop_table('news')
    op.drop_table('user')
    op.drop_table('category')
    # ### end Alembic commands ###
