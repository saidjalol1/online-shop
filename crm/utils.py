from datetime import datetime, timedelta
from shop.models import Order
from expances.models import Expances

current = datetime.now()
def most_sold_product(start_date=None,end_date=None):
    if start_date and end_date is not None:

        start_datetime = datetime.combine(start_date, datetime.min.time())
        end_datetime = datetime.combine(end_date, datetime.max.time())

        orders = Order.objects.filter(status="Unactive", date_added__range = (start_datetime, end_datetime))
        dicts = {}
        for order in orders:
            for i in order.order_items.all():
                dicts.update({
                    f"{i.product.id }": i.quantity
                })
        if dicts:
            max_objects = max(dicts, key=dicts.get)
            return max_objects
        else:
            return None
    else:
        orders = Order.objects.filter(status="Unactive")
        dicts = {}
        for order in orders:
            for i in order.order_items.all():
                dicts.update({
                    f"{i.product.id }": i.quantity
                })
        if dicts:
            max_objects = max(dicts, key=dicts.get)
            return max_objects
        else:
            return None
    

def most_buy_customer(start_date=None, end_date=None):
    if start_date and end_date is not None:

        start_datetime = datetime.combine(start_date, datetime.min.time())
        end_datetime = datetime.combine(end_date, datetime.max.time())

        orders = Order.objects.filter(status="Unactive", date_added__range = (start_datetime, end_datetime))
        orders_per_customer = {}
        for i in orders:
            orders_per_customer.update({
                f"{i.name }": i.overall_price()
            })
        if orders_per_customer:
            max_objects = max(orders_per_customer, key=orders_per_customer.get)
            print(max_objects)
            return max_objects
        else: 
            return None
    else:
        orders = Order.objects.filter(status="Unactive")
        orders_per_customer = {}
        for i in orders:
            orders_per_customer.update({
                f"{i.name }": i.overall_price()
            })
        if orders_per_customer:
            max_objects = max(orders_per_customer, key=orders_per_customer.get)
            return max_objects
        else: 
            return None
        

def debt_sale(start_date=None, end_date=None):
    if start_date and end_date is not None :

        start_datetime = datetime.combine(start_date, datetime.min.time())
        end_datetime = datetime.combine(end_date, datetime.max.time())

        orders = Order.objects.filter(payment_type="Nasiya", date_added__date__range = (start_datetime, end_datetime))
        objects = []
        for i in orders:
            objects.append(i.overall_price())
        value = sum(objects)
        return value
    else:
        orders = Order.objects.filter(payment_type="Nasiya")
        objects = []
        for i in orders:
            objects.append(i.overall_price())
        value = sum(objects)
        return value
        
    
def cash_sale(start_date=None, end_date=None):
    if start_date and end_date is not None :

        start_datetime = datetime.combine(start_date, datetime.min.time())
        end_datetime = datetime.combine(end_date, datetime.max.time())

        orders = Order.objects.filter(payment_type="Naqd", date_added__range = (start_datetime, end_datetime))
        objects = []
        for i in orders:
            objects.append(i.overall_price())
        value = sum(objects)
        return value
    
    else:
        orders = Order.objects.filter(payment_type="Naqd")
        objects = []
        for i in orders:
            objects.append(i.overall_price())
        value = sum(objects)
        return value
    

    
def expances(start_date=None, end_date=None):
    if start_date and end_date is not None :

        start_datetime = datetime.combine(start_date, datetime.min.time())
        end_datetime = datetime.combine(end_date, datetime.max.time())

        orders = Expances.objects.filter(date_added__range = (start_datetime, end_datetime))
        objects = []
        for i in orders:
            objects.append(i.amount)
        value = sum(objects)
        return value
    
    else:
        orders = Expances.objects.all()
        objects = []
        for i in orders:
            objects.append(i.amount)
        value = sum(objects)
        return value