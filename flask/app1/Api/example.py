from flask import Blueprint,request
from datetime import datetime
from app1.models.model import Order,db
api_page = Blueprint('Api', __name__)


@api_page.route('/1', methods=['GET'])
def getAdsData():
    return "welcome to test"

@api_page.route('/order/add', methods=['POST'])
def addOrder():
    if request.is_json:
        data = request.get_json()
        customer_id=data.get("customer_id",None)
        customer_name=data.get("customer_name",None)
        product_name=data.get("product_name",None)
        product_id=data.get("product_id",None)
        amount=data.get("amount",None)
        price=data.get("price",None)
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
    
@api_page.route('/order/modify', methods=['POST'])
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
        db.session.commit()
        print("success")
        return "success_update"
        
    except:
        print("failed")
        db.session.rollback()
        return "Fail to update new issue to your task."
    
