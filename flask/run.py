# from app1 import app
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask,request
from datetime import datetime
# from app1.models.model import Order

# from app1.Api.example import api_page

app = Flask(__name__)
# api_page = Blueprint('Api', __name__)
# 註冊 blueprint
# app.register_blueprint(api_page)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://test:test@localhost:5432/postgres"
db = SQLAlchemy(app)
migrate = Migrate(app,db)

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

@app.route('/1', methods=['GET'])
def getAdsData():
    return "welcome to test"

@app.route('/order/add', methods=['POST'])
def addOrder():
    customer_id=request.values['customer_id']
    customer_name = request.values['customer_name']
    product_name = request.values['product_name']
    product_id = request.values['product_id']
    amount = request.values['amount']
    price = request.values['price']
    # customer_id=1
    # customer_name="larry"
    # product_name="酒精"
    # product_id=2
    # amount=2
    # price=40
    purchaes_time=datetime.now()
    task_order=Order(customer_id=customer_id,customer_name=customer_name,product_name=product_name,product_id=product_id,amount=amount,price=price,purchaes_time=purchaes_time)
    print(task_order)
    try:
        db.session.add(task_order)
        db.session.commit()
        print("success")
        return "success_insert"
        
    except:
        print("failed")
        db.session.rollback()
        return "Fail to add new issue to your task."
    
@app.route('/order/modify', methods=['POST'])
def fixOrder():
    
    if request.is_json:
        # 解析 JSON 資料為 dict ，若不是 JSON，則返回 None
        data = request.get_json()
        print(data)
        customer_name=data.get("customer_name",None)
        del data["customer_name"]
    new_task=Order.query.filter_by(customer_name=customer_name).update(data)
    print(new_task)
    try:
        # db.session.add(new_task)
        db.session.commit()
        print("success")
        return "success_update"
        
    except:
        print("failed")
        db.session.rollback()
        return "Fail to update new issue to your task."
if __name__=="__main__":
    
    app.run(host="0.0.0.0",debug=True)