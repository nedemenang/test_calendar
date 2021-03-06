"""interviewers table

Revision ID: 155171c60cae
Revises: 
Create Date: 2020-04-03 17:16:47.332733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '155171c60cae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('interview',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('candidate', sa.String(length=64), nullable=True),
    sa.Column('interviewer', sa.String(length=64), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('interview')
    # ### end Alembic commands ###
