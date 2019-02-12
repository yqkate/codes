from flask import Flask, request, render_template, redirect
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, func
import pymysql


app = Flask(__name__,
            # template_folder="",  # 指定存放模板的文件夹名称
            static_url_path="/assets",  # "指定访问静态资源的路径
            static_folder="assets"  # 静态文件夹名称
            )
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/project-test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
print(db)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


#+++++++++++++++++++++++++++++++++++++++++++
# 各种表的类
# ........................................
# 门店申请表
class Apply(db.Model):
    __tablename__ = "apply"
    id = db.Column(db.Integer, primary_key=True)
    #门店id
    shop_id = db.Column(db.Integer,nullable=False)
    # 门店名称
    shop_name = db.Column(db.String(255),nullable=False)
    # 门店图片
    shop_img = db.Column(db.String(255),nullable=True)
    # 门店资质证明（营业执照）
    shop_prove = db.Column(db.String(255),nullable=True)
    # 门店营业开始时间
    shop_begin_time = db.Column(db.DATE,nullable=True)
    # 门店营业结束时间
    shop_end_time = db.Column(db.DATE,nullable=True)
    # 门店标签
    shop_tag = db.Column(db.String(255),nullable=True)
    # 申请状态；0：申请中，1：已通过，2：已拒绝
    status = db.Column(db.SmallInteger,nullable=False)
    # 申请备注
    remark = db.Column(db.String(255),nullable=True)
    pass

# ........................................
# 地区表
class Area(db.Model):
    __tablename__="area"
    # 二级地区id
    area_id = db.Column(db.Integer, primary_key=True)
    # 二级地区名称
    area_name = db.Column(db.String(255),nullable=True)
    # 父地区id
    area_pid = db.Column(db.Integer,nullable=True)
    pass


# ........................................
# 商品种类表 关联了门店id
class Category_goods(db.Model):
    __tablename__ = "category_goods"
    id = db.Column(db.Integer, primary_key=True)
    # 商品种类
    category_name = db.Column(db.String(255),nullable=True)
    # 门店id
    shop_id = db.Column(db.Integer,nullable=True)
    pass



# ........................................
# 商品信息表
class Goods_info(db.Model):
    __tablename__ ="goods_info"
    id = db.Column(db.Integer, primary_key=True)
    # 商品名称
    goods_name = db.Column(db.String(255),nullable=False)
    # 商品图片
    goods_image = db.Column(db.String(255),nullable=True)
    # 商品单价
    goods_price = db.Column(db.Float(2),nullable=False)
    # 商品状态（默认为1：开启，0：未开启）
    goods_status = db.Column(db.SmallInteger,nullable=False)
    # 商品分类
    goods_type = db.Column(db.Integer,nullable=False)
    # 商品备注；也就是商品简介
    goods_notes = db.Column(db.String(255),nullable=True)
    pass


# ........................................
# 商品种类表 关联了门店id
class Goods_type(db.Model):
    __tablename__ = "goods_type"
    id = db.Column(db.Integer, primary_key=True)
    # 商品种类
    type_name = db.Column(db.String(255),nullable=True)
    # 门店id
    shop_id = db.Column(db.Integer)
    pass


# ........................................
# 商家账号信息
class Merchant(db.Model):
    __tablename__ = "merchant"
    merchant_id = db.Column(db.Integer,primary_key=True)
    merchant_name = db.Column(db.String(255),nullable=False)
    merchant_pwd = db.Column(db.String(255),nullable=False)
    #商家版状态（0：商家主账号，1：子帐号，2：不开启)
    merchant_status = db.Column(db.Integer,primary_key=True)
    merchant_phone = db.Column(db.String(11),nullable=True)
    pass


# ........................................
# 门店信息和商户信息关联的表
class Merchant_shop(db.Model):
    __tablename__ = "merchant_shop"
    merchant_id = db.Column(db.Integer, primary_key=True)
    shop_id = db.Column(db.Integer,nullable=False)
    remake_name = db.Column(db.String(255),nullable=True)
    pass



# ........................................
# 订单信息表
class Order(db.Model):
    __tablename__="order"
    id = db.Column(db.Integer,primary_key=True)
    # 订单id；格式：年月日(8)+商家id(4)+时分秒(6)+订单号(2)
    order_id = db.Column(db.CHAR(20),
                         nullable=False,
                         primary_key=True,
                         )
    # 门店id
    shop_id = db.Column(db.Integer,nullable=False)
    # userid
    user_id = db.Column(db.Integer,nullable=False)
    # 支付金额
    pay_money = db.Column(db.Float(2),nullable=False)
    # 支付类型
    pay_type = db.Column(db.SmallInteger,nullable=False)
    # 订单交易状态
    status = db.Column(db.SmallInteger,nullable=False)
    # 订单创建时间
    create_time = db.Column(db.DATETIME,nullable=False)
    # 订单更新时间
    update_taime = db.Column(db.DATETIME,nullable=False)
    # 付款时间
    pay_time = db.Column(db.DATETIME,nullable=True)
    # 订单备注
    remark = db.Column(db.String(255),nullable=True)
    # 桌号 0 外带；其他号码：桌号
    table_id = db.Column(db.Integer,nullable=True)
    # 评价状态；0：未评价，1：已评价，2：删除评价
    appraise_status = db.Column(db.Integer,nullable=False)
    # 评价内容
    appraise = db.Column(db.String(255),nullable=True)
    # 评分数值/获赞数值
    appraise_score = db.Column(db.SmallInteger,nullable=True)
    # 买家/用户昵称是否匿名； 0：不匿名，1：匿名；默认为0
    nick_status = db.Column(db.SmallInteger,nullable=True)
    # 买家/用户昵称（不得超过20个字符
    nick = db.Column(db.String(20),nullable=True)
    # 一 对 order_details('多')
    orders_id = db.relationship(
        'Order',
        backref = 'order',
        lazy ='dynamic'
    )



# ........................................
#订单详情表，订单的详情主要就是购买商品的信息，通过订单的id来实现关联
class Order_details(db.Model):
    __tablename__="order_details"
    id = db.Column(db.Integer,primary_key=True)
    # 订单Id 增加外键,引用自order表的order_id主键
    order_id = db.Column(db.Integer,
                         db.ForeignKey('order.order_id'),
                         nullable=True,)
    # 商品id
    goods_id = db.Column(db.Integer,nullable=True)
    # 商品名称
    goods_name = db.Column(db.VARCHAR(255),nullable=True)
    # 图片url地址
    image_url = db.Column(db.VARCHAR(255),nullable=True)
    # 单价
    price = db.Column(db.Float,nullable=True)
    # 商品数量 不为空
    num = db.Column(db.Integer,nullable=False)
    # 订单总价
    count_money = db.Column(db.VARCHAR(255),nullable=True)




# ........................................
# 门店信息表
class Shop_info(db.Model):
    __tablename__ = "shop_info"
    id = db.Column(db.Integer, primary_key=True)
    # 门店名称
    shop_name = db.Column(db.String(255),nullable=True)
    # 门店图片
    shop_img = db.Column(db.String(255),nullable=True)
    # 门店电话：默认为11位手机号，可以为空
    shop_phone = db.Column(db.Integer,nullable=True)
    # 门店状态（0：未注册，1：正常运行，2：审核中，3：未营业，4：商家已删除，不存在）
    shop_status = db.Column(db.SmallInteger,nullable=False)
    # 门店营业开始时间
    shop_begin_time = db.Column(db.DATE, nullable=True)
    # 门店营业结束时间
    shop_end_time = db.Column(db.DATE, nullable=True)
    # 门店标签
    shop_tag = db.Column(db.String(255), nullable=True)
    # 门店简介
    shop_intro = db.Column(db.String(255),nullable=True)
    # 所属地区
    area = db.Column(db.Integer,nullable=True)
    pass



# ........................................
# 用来区分门店的类型
# 例如：中餐，西餐，汉堡，披萨，炸鸡
class type(db.Model):
    __tablename__ = "type"
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(10),nullable=True)
    pass

# ........................................
# 类型和门店关联的表；
# 门店可以属于多个类型；
# 例如：汉堡王，可以是汉堡，也可以是西餐
class type_shop(db.Model):
    __tablename__ = "type_shop"
    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer,nullable=False)
    shop_id = db.Column(db.Integer,nullable=False)
    pass

# ........................................
# 用户信息表
class user_info(db.Model):
    __tablename__ = "user_info"
    id = db.Column(db.Integer, primary_key=True)
    #用户账号；默认用手机号，不得超过11位长度.并且不可重复
    user_name = db.Column(db.String(11),primary_key=True)
    # 用户密码；用哈希值存入
    password = db.Column(db.String(40),nullable=False)
    # 用户性别('M':男,默认,'F',女)
    sex = db.Column(db.Enum('M','F'),nullable=True)
    # 用户昵称(不得超过20个字符)
    nick = db.Column(db.String(20),nullable=True)
    # 用户手机号
    phone = db.Column(db.String(255),nullable=True)
    # 用户头像
    image = db.Column(db.String(255),nullable=True)
    # 用户所在区域
    user_area = db.Column(db.Integer,nullable=True)
    # 创建时间
    create_time = db.Column(db.DATETIME,nullable=True)
    # 更新时间
    update_time = db.Column(db.DATETIME,nullable=True)
    pass

# ........................................
#+++++++++++++++++++++++++++++++++++++++++


#---------------------------------------------
# localhost:5000/
# 主页部分
@app.route("/")
@app.route("/<name>")
def html(name=None):
    if name is None:
        return render_template("index.html")
    return render_template(name)
#-------------------------------------------

#----------------------------------------
# localhost:5000/cart-page.html
# 购物车后台部分
@app.route('/cart-page')
def cart_page_viwes():
    # # 1. 获取当前订单号
    # order_id = request.args['order_id']
    # # 2. 根据订单号,查询出订单下菜品详情
    # goods = db.session.query(order_details)
    pass

#---------------------------------------
if __name__ == "__main__":
    # app.run(debug=True,
    #         # port=5555,  # 开放访问的端口号,默认为50000
    #         # host="0.0.0.0"  # host:指定访问到本项目的地址,0.0.0.0表示局域网内任何机器都可以访问到当前本项目,其他访问班级项目时需要使用ip地址
    #         )

    manager.run()
