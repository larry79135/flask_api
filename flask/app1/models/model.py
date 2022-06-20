# from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime
# from flask_migrate import Migrate
from run import db

# app= Flask(__name__)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://test:test@localhost:5432/postgres"

# db = SQLAlchemy(app)
# # # 绑定app和数据库
# migrate = Migrate(app,db)

# db.init_app(app)
# 模型( model )定義
class Order(db.Model):
    __tablename__='order1'
    order_id=db.Column( db.Integer, autoincrement=True, primary_key=True)
    customer_name=db.Column(db.String(30), unique=False, nullable=False)
    customer_id=db.Column(db.Integer, unique=True,nullable=False)
    product_name=db.Column(db.String(100), unique=False, nullable=False)
    product_id=db.Column(db.Integer, unique=False,nullable=False)
    amount=db.Column(db.Integer, nullable=False)
    price=db.Column(db.Integer, nullable=False)
    purchaes_time=db.Column(db.DateTime, default=datetime.now)
    
    def __init__(self, customer_name, customer_id, product_name, product_id, amount,price,purchaes_time):
        self.customer_name = customer_name
        self.customer_id = customer_id
        self.product_name = product_name
        self.product_id = product_id
        self.amount = amount
        self.price=price
        self.purchaes_time=purchaes_time

# db.create_all()

# if __name__=="__main__":
#     # app = Flask(__name__)
#     # db = SQLAlchemy(app)
#     migrate = Migrate(app, db)
#     db.init_app(app)
#     migrate.init_app(app=app,db=db)
#     db.create_all()
    