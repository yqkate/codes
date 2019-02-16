"""empty message

Revision ID: e8bda08547ff
Revises: 
Create Date: 2019-02-15 00:19:32.358924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8bda08547ff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('apply',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shop_id', sa.Integer(), nullable=False),
    sa.Column('shop_name', sa.String(length=255), nullable=False),
    sa.Column('shop_img', sa.String(length=255), nullable=True),
    sa.Column('shop_prove', sa.String(length=255), nullable=True),
    sa.Column('shop_begin_time', sa.DATE(), nullable=True),
    sa.Column('shop_end_time', sa.DATE(), nullable=True),
    sa.Column('shop_tag', sa.String(length=255), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=False),
    sa.Column('remark', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('area',
    sa.Column('area_id', sa.Integer(), nullable=False),
    sa.Column('area_name', sa.String(length=255), nullable=True),
    sa.Column('area_pid', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('area_id')
    )
    op.create_table('category_goods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=255), nullable=True),
    sa.Column('shop_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('goods_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('goods_name', sa.String(length=255), nullable=False),
    sa.Column('goods_image', sa.String(length=255), nullable=True),
    sa.Column('goods_price', sa.Float(precision=2), nullable=False),
    sa.Column('goods_status', sa.SmallInteger(), nullable=False),
    sa.Column('goods_type', sa.Integer(), nullable=False),
    sa.Column('goods_notes', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('goods_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type_name', sa.String(length=255), nullable=True),
    sa.Column('shop_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('merchant',
    sa.Column('merchant_id', sa.Integer(), nullable=False),
    sa.Column('merchant_name', sa.String(length=255), nullable=False),
    sa.Column('merchant_pwd', sa.String(length=255), nullable=False),
    sa.Column('merchant_status', sa.Integer(), nullable=False),
    sa.Column('merchant_phone', sa.String(length=11), nullable=True),
    sa.PrimaryKeyConstraint('merchant_id', 'merchant_status')
    )
    op.create_table('merchant_shop',
    sa.Column('merchant_id', sa.Integer(), nullable=False),
    sa.Column('shop_id', sa.Integer(), nullable=False),
    sa.Column('remake_name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('merchant_id')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.CHAR(length=20), nullable=False),
    sa.Column('shop_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('pay_money', sa.Float(precision=2), nullable=False),
    sa.Column('pay_type', sa.SmallInteger(), nullable=False),
    sa.Column('status', sa.SmallInteger(), nullable=False),
    sa.Column('create_time', sa.DATETIME(), nullable=False),
    sa.Column('update_taime', sa.DATETIME(), nullable=False),
    sa.Column('pay_time', sa.DATETIME(), nullable=True),
    sa.Column('remark', sa.String(length=255), nullable=True),
    sa.Column('table_id', sa.Integer(), nullable=True),
    sa.Column('appraise_status', sa.Integer(), nullable=False),
    sa.Column('appraise', sa.String(length=255), nullable=True),
    sa.Column('appraise_score', sa.SmallInteger(), nullable=True),
    sa.Column('nick_status', sa.SmallInteger(), nullable=True),
    sa.Column('nick', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shop_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shop_name', sa.String(length=255), nullable=True),
    sa.Column('shop_img', sa.String(length=255), nullable=True),
    sa.Column('shop_phone', sa.Integer(), nullable=True),
    sa.Column('shop_status', sa.SmallInteger(), nullable=False),
    sa.Column('shop_begin_time', sa.DATE(), nullable=True),
    sa.Column('shop_end_time', sa.DATE(), nullable=True),
    sa.Column('shop_tag', sa.String(length=255), nullable=True),
    sa.Column('shop_intro', sa.String(length=255), nullable=True),
    sa.Column('area', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type_name', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('type_shop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('shop_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=11), nullable=False),
    sa.Column('password', sa.String(length=40), nullable=False),
    sa.Column('sex', sa.Enum('M', 'F'), nullable=True),
    sa.Column('nick', sa.String(length=20), nullable=True),
    sa.Column('phone', sa.String(length=255), nullable=True),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('user_area', sa.Integer(), nullable=True),
    sa.Column('create_time', sa.DATETIME(), nullable=True),
    sa.Column('update_time', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'user_name')
    )
    op.create_table('order_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('goods_id', sa.Integer(), nullable=True),
    sa.Column('goods_name', sa.String(length=255), nullable=True),
    sa.Column('image_url', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('num', sa.Integer(), nullable=False),
    sa.Column('count_money', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_details')
    op.drop_table('user_info')
    op.drop_table('type_shop')
    op.drop_table('type')
    op.drop_table('shop_info')
    op.drop_table('order')
    op.drop_table('merchant_shop')
    op.drop_table('merchant')
    op.drop_table('goods_type')
    op.drop_table('goods_info')
    op.drop_table('category_goods')
    op.drop_table('area')
    op.drop_table('apply')
    # ### end Alembic commands ###
