from django.db import models
from django.contrib.auth.models import User



client_status = (
        (-4, 'نقل وتحميل'),
        (-3, 'صراف'),
        (-2, 'مساهم'),
        (-1, 'نثريات'),
        (0, 'المالك'),
        (1, 'موظف'),
        (2, 'مورد'),
        (3, 'زبون'),
    )
currencies = (
     (0, 'دولار أمريكي'),
     (1, 'ليرة سورية')
    )

invoice_status = (
    (1, 'بيع'),
    (2, 'شراء'),
    (3, 'راتب'),
    (4, 'تصريف'),
    (5, 'مرتجع بيع'),
    (6, 'مرتجع شراء')
    )



# Create your models here.
'''
class Client_Status(models.Model):
    client_stat_name = models.CharField(max_length=11
    ,choices=client_status)

class Currencies(models.Model):
    curr_name = models.CharField(max_length=15)
    curr_sym = models.CharField(max_length=5)


class Invoice_Status(models.Model):
    inv_stat_name = models.CharField(max_length=25)
'''
    

class Clients(models.Model):
    client_name = models.CharField(max_length=70)
    client_stat = models.SmallIntegerField(choices=client_status)
    client_address = models.TextField(null=True)
    client_email = models.EmailField(max_length=70, null=True)
    client_phone = models.CharField(max_length=16, null=True)
    client_cell_phone = models.CharField(max_length=16, null=True)

    def serialize(context):
        all =[]
        for data in context:
            all.append({'id': data.id, 'name': data.client_name,
             'status': data.client_stat , 'address': data.client_address ,'email': data.client_email ,
             'phone': data.client_phone , 'cell_phone': data.client_cell_phone})
        return all

class Users(models.Model):
    client = models.ForeignKey(Clients, null=True, on_delete=models.SET_NULL)
    user_name = models.CharField(max_length=25)
    pass_word = models.CharField(max_length=50)
    user_permissions = models.IntegerField()

    def serialize(context):
        all =[]
        for data in context:
            all.append({'id': data.id, 'client': data.client,
             'name': data.user_name , 'password': data.pass_word ,'permissions': data.user_permissions })
        return all

class Accounts(models.Model):
    curr = models.SmallIntegerField(choices=currencies)
    amount = models.FloatField(default=0.00)
    client = models.ForeignKey(Clients, null=True, on_delete=models.SET_NULL)
    
    def serialize(context):
        all =[]
        for data in context:
            all.append({'id': data.id, 'curr': data.curr,
             'amount': data.amount , 'client': data.client })
        return all

    class Meta:
        unique_together = ('curr', 'client',)

class Units(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def serialize(context):
        all =[]
        for data in context:
            all.append({'id': data.id, 'name': data.name})
        return all

class Items(models.Model):
    name = models.CharField(max_length=50, unique=True)
    specs = models.TextField()
    unit = models.ForeignKey(Units, null=True, on_delete=models.SET_NULL)
    minimum_quantity = models.FloatField()
    cost =models.FloatField()
    minimum_price = models.FloatField()
    normal_price = models.FloatField()
    status = models.BooleanField(choices=((False, 'صنف متداول'), (True, 'صنف غير متداول')))

    def serialize(context):
        all =[]
        for data in context:
            all.append({'id': data.id, 'name': data.name,
             'specs': data.specs , 'unit': data.unit.id ,'minimum_quantity': data.minimum_quantity ,
             'cost': data.cost , 'minimum_price': data.minimum_price,
             'normal_price': data.normal_price , 'status': data.status})
        return all

class Stores(models.Model):
    name = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=50)
    specs = models.TextField()
    status = models.SmallIntegerField(choices=((0, 'نشط'), (2, 'غير نشط')) )

    def serialize(context):
        all =[]
        for data in context:
            all.append({'id': data.id, 'name': data.name,
             'location': data.location , 'specs': data.specs ,
             'status': data.status })
        return all
    
    def startonly():
        store = Stores(name='المستودع الرئيسي', location='',specs='',status=0)
        store.save()

class Stocks(models.Model):
    item = models.ForeignKey(Items, null=True, on_delete=models.SET_NULL)
    store = models.ForeignKey(Stores,on_delete=models.SET_DEFAULT ,default= 1)
    quantity = models.FloatField(default= 0.00)
    last_in_date = models.DateField(null=True)
    last_out_date = models.DateField(null=True)

    def serialize(context):
        all =[]
        for data in context:
            all.append({'id': data.id, 'item':data.item, 'store': data.store,
             'quantity': data.quantity , 'last_in_date': data.last_in_date ,
             'last_out_date': data.last_out_date })
        return all

    class Meta:
        unique_together = ('store', 'item',)


class Statements(models.Model):
    statement_date = models.DateField(null=True)
    account = models.ForeignKey(Accounts, null=True, on_delete=models.SET_NULL)
    amount = models.FloatField()
    amount_type = models.SmallIntegerField(choices=((0, 'Money'), (1, 'Goods')))
    statement_description = models.TextField()
    amount_direction = models.SmallIntegerField(choices=((0, 'Income'), (1, 'Outlay')))
    exchange_rate = models.FloatField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def serialize(context):
        all =[]
        for data in context:
            all.append({'id': data.id, 'date': data.statement_date,
             'account': data.account , 'amount': data.amount ,'amount_type': data.amount_type ,
             'description': data.statement_description , 'amount_direction': data.amount_direction,
             'exchange_rate': data.exchange_rate , 'user': data.user})
        return all

class Invoices(models.Model):
    inv_date = models.DateField()
    inv_stat = models.SmallIntegerField(choices=invoice_status)
    payment_date = models.DateField(null=True)
    account = models.ForeignKey(Accounts, null=True, on_delete=models.SET_NULL)
    store = models.ForeignKey(Stores, null=True, on_delete=models.SET_NULL)
    discount = models.FloatField(null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    ref_number = models.CharField(max_length=25)
    delivery = models.FloatField(null=True)

    def serialize(context):
        all =[]
        for data in context:
            all.append({'id': data.id, 'date': data.inv_date,
             'status': data.inv_stat , 'payment_date': data.payment_date ,'account': data.account ,
             'store': data.store , 'discount': data.discount,
             'ref_number': data.ref_number , 'user': data.user, 'delivery': data.delivery})
        return all

class Statements_Invoices(models.Model):
    statement = models.ForeignKey(Statements, null=True, on_delete=models.SET_NULL)
    inv = models.ForeignKey(Invoices, null=True, on_delete=models.SET_NULL)

    def serialize(context):
        all =[]
        for data in context:
            all.append({'id': data.id, 'statement': data.statement,
             'inv': data.inv })
        return all
    
class Inv_Quantities(models.Model):
    inv = models.ForeignKey(Invoices, null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Items, null=True, on_delete=models.SET_NULL)
    item_price = models.FloatField()
    item_cost = models.FloatField(default= 0.00)
    quantity = models.FloatField()
    discount_for_item = models.FloatField()

    def serialize(context):
        all =[]
        for data in context:
            all.append({'id': data.id, 'inv': data.inv,
             'item': data.item , 'item_price': data.item_price ,'item_cost': data.item_cost ,
             'quantity': data.quantity , 'discount': data.discount_for_item})
        return all

class Inventory(models.Model):
    inventory_date = models.DateField()
    cash = models.FloatField()
    stock = models.FloatField()
    debtors = models.FloatField()
    fund = models.FloatField()
    creditors = models.FloatField()
    profit = models.FloatField()
    notes = models.TextField(null=True)

    def serialize(context):
        all =[]
        for data in context:
            all.append({'id': data.id, 'date': data.inventory_date,
             'cash': data.cash , 'stock': data.stock ,'debtors': data.debtors ,
             'fund': data.fund , 'creditors': data.creditors,
             'profit': data.profit , 'notes': data.notes})
        return all

class Operations(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    operation_date = models.DateTimeField()
    operation_description = models.TextField()

    def serialize(context):
        all =[]
        for data in context:
            all.append({'id': data.id, 'user': data.user,
             'date': data.operation_date , 'description': data.operation_description })
        return all

