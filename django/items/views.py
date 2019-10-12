from django.http import HttpResponse, JsonResponse
from main.models import Items,Stores,Stocks,Units
from rest_framework.decorators import api_view
from json import loads

# Create your views here.
@api_view(["GET"])
def items(request):

        context = Items.objects.all()
        context = Items.serialize(context)  
        return JsonResponse(context ,safe=False)

@api_view(["POST"])
def additem(request):
        
        req = loads(request.body)
        name = req["name"]
        specs = req["specs"]
        unit = req["unit"]
        minimum_quantity = req["minimum_quantity"]
        cost = req["cost"]
        minimum_price = req["minimum_price"]
        normal_price = req["normal_price"]
        status = req["status"]

        quantity = req["quantity"]
        unit = Units.objects.get(id=unit) 
        
        item = Items(name=name, specs=specs , unit=unit, minimum_price=minimum_price,
        minimum_quantity=minimum_quantity, cost=cost, normal_price=normal_price, status=status)
        item.save()
        
        items_stors(item,quantity)
        return HttpResponse("created")

@api_view(["PUT"])
def edititem(request, id):
               
        req = loads(request.body)

        name = req["name"]
        specs = req["specs"]
        unit = req["unit"]
        minimum_quantity = req["minimum_quantity"]
        minimum_price = req["minimum_price"]
        normal_price = req["normal_price"]
        status = req["status"]

        
        item = Items.objects.filter(id=req['id'])
        item.update(name=name, specs=specs , unit=unit, minimum_price=minimum_price,
        minimum_quantity=minimum_quantity, normal_price=normal_price, status=status)
        
        return HttpResponse("edited")

def items_stors(item, quantity):
        
        #s=con.query("select store_id from stores order by store_id asc;")
        id_stores= Stores.objects.all().order_by('id')
        for store in id_stores:
                id_items = Items.objects.all().order_by('-id')
                
                try:
                        for item in id_items:
                                stock = Stocks(item=item, store=store)
                                stock.save()                        
                except:
                        pass        
        
        stock = Stocks.objects.filter(item=item, store=1)
        stock.update(quantity=quantity)
        
        '''
        store=con.query("select store_name from stores where store_id=1")
        QMessageBox.information(self,"تنبيه", "تم اضافة الكمية للمستودع ({})".format(store[0][0]))
        '''