"""final

Revision ID: c4cf6435f422
Revises: 90c9c94c68fb
Create Date: 2024-03-08 07:51:01.437789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4cf6435f422'
down_revision = '90c9c94c68fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bookings', schema=None) as batch_op:
        batch_op.alter_column('start_date',
               existing_type=sa.DATE(),
               type_=sa.String(),
               existing_nullable=False)
        batch_op.alter_column('end_date',
               existing_type=sa.DATE(),
               type_=sa.String(),
               existing_nullable=False)
        batch_op.alter_column('start_time',
               existing_type=sa.TIME(),
               type_=sa.String(),
               existing_nullable=False)
        batch_op.alter_column('end_time',
               existing_type=sa.TIME(),
               type_=sa.String(),
               existing_nullable=False)

    with op.batch_alter_table('cars', schema=None) as batch_op:
        batch_op.alter_column('availability_status',
               existing_type=sa.BOOLEAN(),
               type_=sa.String(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cars', schema=None) as batch_op:
        batch_op.alter_column('availability_status',
               existing_type=sa.String(),
               type_=sa.BOOLEAN(),
               existing_nullable=True)

    with op.batch_alter_table('bookings', schema=None) as batch_op:
        batch_op.alter_column('end_time',
               existing_type=sa.String(),
               type_=sa.TIME(),
               existing_nullable=False)
        batch_op.alter_column('start_time',
               existing_type=sa.String(),
               type_=sa.TIME(),
               existing_nullable=False)
        batch_op.alter_column('end_date',
               existing_type=sa.String(),
               type_=sa.DATE(),
               existing_nullable=False)
        batch_op.alter_column('start_date',
               existing_type=sa.String(),
               type_=sa.DATE(),
               existing_nullable=False)

    # ### end Alembic commands ###
