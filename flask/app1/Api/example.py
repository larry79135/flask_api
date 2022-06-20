from flask import Blueprint
from datetime import datetime
from app1.models.model import Order,db
# from flask import Flask
# from run import app
api_page = Blueprint('Api', __name__)
# app = Flask(__name__)
# 註冊 blueprint
# app.register_blueprint(api_page)



@api_page.route('/1', methods=['GET'])
def getAdsData():
    return "welcome to test"

@api_page.route('/order', methods=['POST'])
def addOrder():
    # customer_id=request.values['customer_id']
    # customer_name = request.values['customer_name']
    # product_name = request.values['product_name']
    # product_id = request.values['product_id']
    # amount = request.values['amount']
    # price = request.values['price']
    customer_id=1
    customer_name="larry"
    product_name="酒精"
    product_id=2
    amount=2
    price=40
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
    
