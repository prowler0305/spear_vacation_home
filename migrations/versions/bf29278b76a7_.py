"""empty message

Revision ID: bf29278b76a7
Revises: 845692322d31
Create Date: 2021-04-15 20:56:36.172849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf29278b76a7'
down_revision = '845692322d31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('suggestions', sa.Column('suggestion_category', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('suggestions', 'suggestion_category')
    # ### end Alembic commands ###