"""empty message

Revision ID: 2be5fb93eb01
Revises: 6e7cb314a1e6
Create Date: 2018-04-21 05:07:52.848726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2be5fb93eb01'
down_revision = '6e7cb314a1e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('refresh_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('jti', sa.String(length=36), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('account_id'),
    sa.UniqueConstraint('jti')
    )
    op.add_column('account', sa.Column('email', sa.String(length=60)))
    op.add_column('account', sa.Column('password', sa.String(length=256)))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'account', type_='unique')
    op.drop_column('account', 'password')
    op.drop_column('account', 'email')
    op.drop_table('refresh_token')
    # ### end Alembic commands ###
