"""empty message

Revision ID: dc8288d34999
Revises: 
Create Date: 2019-02-22 20:22:13.503261

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dc8288d34999'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('area',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('area_id', sa.Integer(), nullable=False),
    sa.Column('area_name', sa.String(length=10), nullable=False),
    sa.Column('area_pid', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('area_id')
    )
    op.create_table('classify',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('classify_name', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('merchant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('passwd', sa.String(length=40), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('phone', sa.String(length=11), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_merchant_name'), 'merchant', ['name'], unique=True)
    op.create_table('shop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shop_name', sa.String(length=10), nullable=False),
    sa.Column('shop_img', sa.String(length=100), nullable=True),
    sa.Column('shop_phone', sa.String(length=11), nullable=True),
    sa.Column('shop_status', sa.Integer(), nullable=False),
    sa.Column('shop_begin_time', sa.Time(), nullable=True),
    sa.Column('shop_end_time', sa.Time(), nullable=True),
    sa.Column('shop_tag', sa.String(length=100), nullable=True),
    sa.Column('shop_intro', sa.String(length=100), nullable=True),
    sa.Column('area', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=11), nullable=False),
    sa.Column('password', sa.String(length=40), nullable=False),
    sa.Column('sex', sa.Enum('M', 'F'), nullable=False),
    sa.Column('nick', sa.String(length=20), nullable=True),
    sa.Column('phone', sa.String(length=11), nullable=True),
    sa.Column('image', sa.String(length=100), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=False),
    sa.Column('update_time', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_index(op.f('ix_user_user_name'), 'user', ['user_name'], unique=True)
    op.create_table('apply',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shop_id', sa.Integer(), nullable=True),
    sa.Column('shop_name', sa.String(length=10), nullable=False),
    sa.Column('shop_img', sa.String(length=100), nullable=True),
    sa.Column('shop_prove', sa.String(length=100), nullable=True),
    sa.Column('shop_begin_time', sa.Time(), nullable=True),
    sa.Column('shop_end_time', sa.Time(), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=False),
    sa.Column('remark', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['shop_id'], ['shop.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('classify_shop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('classify_id', sa.Integer(), nullable=True),
    sa.Column('shop_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['classify_id'], ['classify.id'], ),
    sa.ForeignKeyConstraint(['shop_id'], ['shop.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('goods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shop_id', sa.Integer(), nullable=True),
    sa.Column('goods_name', sa.String(length=10), nullable=False),
    sa.Column('goods_image', sa.String(length=100), nullable=False),
    sa.Column('goods_price', mysql.FLOAT(precision=10, scale=2), nullable=False),
    sa.Column('goods_status', sa.SmallInteger(), nullable=False),
    sa.Column('goods_notes', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['shop_id'], ['shop.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('menu_name', sa.String(length=10), nullable=False),
    sa.Column('shop_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['shop_id'], ['shop.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('merchant_shop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('merchant_id', sa.Integer(), nullable=True),
    sa.Column('shop_id', sa.Integer(), nullable=True),
    sa.Column('remake_name', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['merchant_id'], ['merchant.id'], ),
    sa.ForeignKeyConstraint(['shop_id'], ['shop.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.String(length=24), nullable=False),
    sa.Column('shop_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pay_money', mysql.FLOAT(precision=10, scale=2), nullable=True),
    sa.Column('pay_type', sa.SmallInteger(), nullable=False),
    sa.Column('status', sa.SmallInteger(), nullable=False),
    sa.Column('shop_status', sa.SmallInteger(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=False),
    sa.Column('update_time', sa.DateTime(), nullable=False),
    sa.Column('pay_time', sa.DateTime(), nullable=True),
    sa.Column('remark', sa.String(length=100), nullable=True),
    sa.Column('table_id', sa.String(length=100), nullable=True),
    sa.Column('appraise_status', sa.SmallInteger(), nullable=True),
    sa.Column('appraise', sa.String(length=100), nullable=True),
    sa.Column('appraise_score', sa.SmallInteger(), nullable=True),
    sa.Column('nick_status', sa.SmallInteger(), nullable=True),
    sa.Column('nick', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['shop_id'], ['shop.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_order_order_id'), 'order', ['order_id'], unique=True)
    op.create_table('order_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.String(length=24), nullable=True),
    sa.Column('goods_id', sa.Integer(), nullable=True),
    sa.Column('goods_name', sa.String(length=20), nullable=False),
    sa.Column('image_url', sa.String(length=100), nullable=True),
    sa.Column('price', mysql.FLOAT(precision=10, scale=2), nullable=False),
    sa.Column('num', sa.Integer(), nullable=False),
    sa.Column('count_money', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['goods_id'], ['goods.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order.order_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_details')
    op.drop_index(op.f('ix_order_order_id'), table_name='order')
    op.drop_table('order')
    op.drop_table('merchant_shop')
    op.drop_table('menu')
    op.drop_table('goods')
    op.drop_table('classify_shop')
    op.drop_table('apply')
    op.drop_index(op.f('ix_user_user_name'), table_name='user')
    op.drop_table('user')
    op.drop_table('shop')
    op.drop_index(op.f('ix_merchant_name'), table_name='merchant')
    op.drop_table('merchant')
    op.drop_table('classify')
    op.drop_table('area')
    # ### end Alembic commands ###
