"""Added video_file table

Revision ID: fb245977373f
Revises: 6a4d853aabce
Create Date: 2021-01-21 22:47:20.335928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb245977373f'
down_revision = '6a4d853aabce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('video_file',
    sa.Column('device_id', sa.String(), nullable=False),
    sa.Column('video_name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['device_id'], ['device.id'], ),
    sa.PrimaryKeyConstraint('device_id', 'video_name')
    )
    op.alter_column('statistic', 'people_total',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('statistic', 'people_with_mask',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('statistic', 'people_without_mask',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('statistic', 'people_without_mask',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('statistic', 'people_with_mask',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('statistic', 'people_total',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_table('video_file')
    # ### end Alembic commands ###