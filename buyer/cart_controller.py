from mainadmin.models import *
import uuid


class CretaeCart():
    def createcartto(self,**kwargs):
        try:
            uuid_id = kwargs['cartdetails'].get('uuid')
            productid = kwargs['cartdetails'].get('productid')
            user = kwargs['user']
            print(user)
            newd = uuid.uuid1().int
            print(str(newd)[:8])
            product = Product.objects.get(id=productid)


            if user.is_authenticated:
                customer = Customer.objects.filter(user=user)
                if customer.exists():
                    customerget = Customer.objects.get(user=user)
                    getorder = Order.objects.filter(customer=customerget,current_status=False)
                    if getorder.exists():
                        print("order exist")
                        orderis = Order.objects.get(customer=customerget,current_status=False)
                        orderitem, created = OrderItems.objects.get_or_create(order=orderis,product=product)
                        orderitem.qty = orderitem.qty + 1
                        
                        product.available_stock = product.available_stock - 1
                        orderitem.save()
                        product.save()
                    else:
                        print("not Exist")
                        order_create = Order.objects.create(customer=customerget,order_id=str(newd)[:10])
                        orderitem , created= OrderItems.objects.get_or_create(order=order_create,product=product)
                        orderitem.qty = orderitem.qty + 1
                        print(product.available_stock)
                        product.available_stock = product.available_stock - 1
                        orderitem.save()
                        product.save()
                else:
                    create_customer = Customer.objects.create(user=user,custome_id=uuid_id)
                    order = Order.objects.filter(customer=create_customer,current_status=False)
                    if order.exists():
                        print("order exist")
                        orderf = Order.objects.get(customer=create_customer,current_status=False)
                        orderitem, created = OrderItems.objects.get_or_create(order=orderf,product=product)
                        orderitem.qty = orderitem.qty + 1
                        print(product.available_stock)

                        product.available_stock = product.available_stock - 1
                        orderitem.save()
                        product.save()
                    else:
                        order_create = Order.objects.create(customer=create_customer,order_id=str(newd)[:10])
                        orderitem, created = OrderItems.objects.get_or_create(order=order_create,product=product)
                        orderitem.qty = orderitem.qty + 1
                        print(product.available_stock)

                        product.available_stock = product.available_stock - 1
                        orderitem.save()
                        product.save()
            else:
                print("no")
                customer = Customer.objects.filter(custome_id=uuid_id)
                if customer.exists():
                    customerget = Customer.objects.get(custome_id=uuid_id)
                    getorder = Order.objects.filter(customer=customerget,current_status=False)
                    if getorder.exists():
                        print("order exist")
                        orderis = Order.objects.get(customer=customerget,current_status=False)
                        orderitem, created = OrderItems.objects.get_or_create(order=orderis,product=product)
                        orderitem.qty = orderitem.qty + 1
                        print(product.available_stock)

                        product.available_stock = product.available_stock - 1
                        orderitem.save()
                        product.save()
                    else:
                        print("not Exist")
                        order_create = Order.objects.create(customer=customerget,order_id=str(newd)[:10])
                        orderitem, created = OrderItems.objects.get_or_create(order=order_create,product=product)
                        orderitem.qty = orderitem.qty + 1
                        print(product.available_stock)

                        product.available_stock = product.available_stock - 1
                        orderitem.save()
                        product.save()
                else:
                    create_customer = Customer.objects.create(custome_id=uuid_id)
                    order = Order.objects.filter(customer=create_customer,current_status=False)
                    if order.exists():
                        orderf = Order.objects.get(customer=create_customer,current_status=False)
                        orderitem, created = OrderItems.objects.get_or_create(order=orderf,product=product)
                        orderitem.qty = orderitem.qty + 1
                        print(product.available_stock)

                        product.available_stock = product.available_stock - 1
                        orderitem.save()
                        product.save()
                    else:
                        order_create = Order.objects.create(customer=create_customer,order_id=str(newd)[:10])
                        orderitem, created = OrderItems.objects.get_or_create(order=order_create,product=product)
                        orderitem.qty = orderitem.qty + 1
                        print(product.available_stock)

                        product.available_stock = product.available_stock - 1
                        orderitem.save()
                        product.save()
        except Exception as e:
            print(e)

    