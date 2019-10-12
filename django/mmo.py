from peewee import *
from db import con_db

con = con_db(1)
database = con.database

#db = MySQLDatabase(database=database, host=host, user=user, password=password)
db = SqliteDatabase(database)




#######
class client_status(Model):
    client_stat_id = PrimaryKeyField(null=True)
    client_stat_name = CharField(max_length=11)

    class Meta:
        database = db
        primary_key = False


########
class currencies(Model):
    curr_id = PrimaryKeyField(null=True)
    curr_name = CharField(max_length=15)
    curr_sym = CharField(max_length=5)

    class Meta:
        database = db
        primary_key = False


########
class invoice_status(Model):
    inv_stat_id = PrimaryKeyField(null=True)
    inv_stat_name = CharField(max_length=25)

    class Meta:
        database = db
        primary_key = False


########
class clients(Model):
    client_id = PrimaryKeyField(null=True)
    client_name = CharField(max_length=70)
    client_stat = ForeignKeyField(client_status, column_name="client_stat")
    client_address = TextField(null=True)
    client_email = CharField(max_length=70, null=True)
    client_phone = CharField(max_length=16, null=True)
    client_cell_phone = CharField(max_length=16, null=True)

    class Meta:
        database = db
        primary_key = False


########
class users(Model):
    user_id = PrimaryKeyField(null=True)
    client_id = ForeignKeyField(clients)
    user_name = CharField(max_length=25)
    pass_word = CharField(max_length=50)
    user_permissions = IntegerField()

    class Meta:
        database = db
        primary_key = False


########
class accounts(Model):
    account_id = PrimaryKeyField(null=True)
    curr_id = ForeignKeyField(currencies)
    amount = FloatField(constraints=[SQL('DEFAULT 0.00')])
    client_id = ForeignKeyField(clients)

    class Meta:
        database = db
        primary_key = False


accounts.add_index(accounts.curr_id, accounts.client_id, unique=True)


########
class units(Model):
    unit_id = PrimaryKeyField(null=True)
    unit_name = CharField(max_length=15, unique=True)

    class Meta:
        database = db
        primary_key = False


########
class items(Model):
    item_id = PrimaryKeyField(null=True)
    item_name = CharField(max_length=50, unique=True)
    item_specs = TextField()
    unit = ForeignKeyField(units, column_name="unit")
    minimum_quantity = FloatField()
    item_cost = FloatField()
    minimum_price = FloatField()
    normal_price = FloatField()
    item_status = SmallIntegerField(choices=((0, 'صنف متداول'), (2, 'صنف غير متداول')))

    class Meta:
        database = db
        primary_key = False


########
class stores(Model):
    store_id = PrimaryKeyField(null=True)
    store_name = CharField(50, unique=True)
    store_location = CharField(50)
    store_spec = TextField()
    store_status = SmallIntegerField(help_text='0: active 2: disable')

    class Meta:
        database = db
        primary_key = False


########
class stocks(Model):
    item_id = ForeignKeyField(items)
    store_id = ForeignKeyField(stores, constraints=[SQL('DEFAULT 1')])
    quantity = FloatField(constraints=[SQL('DEFAULT 0.00')])
    last_in_date = DateField(null=True)
    last_out_date = DateField(null=True)

    class Meta:
        database = db
        primary_key = False


stocks.add_index(stocks.store_id, stocks.item_id, unique=True)


########
class statements(Model):
    statement_id = PrimaryKeyField(null=True)
    statement_date = DateField(null=True)
    account_id = ForeignKeyField(accounts)
    amount = FloatField()
    amount_type = SmallIntegerField(choices=((0, 'Money'), (1, 'Goods')))
    statement_description = TextField()
    amount_direction = SmallIntegerField(choices=((0, 'Income'), (1, 'Outlay')))
    exchange_rate = FloatField()
    user_id = ForeignKeyField(users)

    class Meta:
        database = db
        primary_key = False


########
class invoices(Model):
    inv_id = PrimaryKeyField(null=True)
    inv_date = DateField()
    inv_stat_id = ForeignKeyField(invoice_status)
    payment_date = DateField(null=True)
    account_id = ForeignKeyField(accounts)
    store_id = ForeignKeyField(stores)
    discount = FloatField(null=True)
    user_id = ForeignKeyField(users)
    ref_number = CharField(max_length=25)
    delivery = FloatField(null=True)

    class Meta:
        database = db
        primary_key = False


########
class statements_invoices(Model):
    statement_id = ForeignKeyField(statements)
    inv_id = ForeignKeyField(invoices)

    class Meta:
        database = db
        primary_key = False


########
class inv_quantities(Model):
    inv_id = ForeignKeyField(invoices)
    item_id = ForeignKeyField(items)
    item_price = FloatField()
    item_cost = FloatField(constraints=[SQL('DEFAULT 0.00')])
    quantity = FloatField()
    discount_for_item = FloatField()

    class Meta:
        database = db
        primary_key = False


########
class inventory(Model):
    inventory_date = DateField()
    cash = FloatField()
    stock = FloatField()
    debtors = FloatField()
    fund = FloatField()
    creditors = FloatField()
    profit = FloatField()
    notes = TextField(null=True)

    class Meta:
        database = db
        primary_key = False


class operations(Model):
    user_id = ForeignKeyField(users)
    operation_date = DateTimeField()
    operation_description = TextField()

    class Meta:
        database = db




db.connect()
db.create_tables([users, units, stores, stocks, statements_invoices, statements, items, invoices,
                  inv_quantities, clients, accounts, inventory, invoice_status, client_status,
                  currencies, operations])

try:

    ##### 'client_status'  #####
    con.query("INSERT INTO `client_status` (`client_stat_id`, `client_stat_name`) VALUES  "
              "('-4', 'نقل وتحميل')"
              ",('-3', 'صراف')"
              ",('-2', 'مساهم')"
              ",('-1', 'نثريات')"
              ",(4, 'المالك')"
              ",('1', 'موظف')"
              ",('2', 'مورد')"
              ",('3', 'زبون');"
              )
    con.mydb.commit()

    con.query("UPDATE `client_status` SET `client_stat_id` = '0' WHERE `client_status`.`client_stat_id` = 4;")
    con.mydb.commit()

    ##### 'currencies'  #####
    con.query("INSERT INTO `currencies` (`curr_id`, `curr_name`, `curr_sym`) VALUES"
              " (2, 'دولار أمريكي', '$')"
              ",(1, 'ليرة سورية', 'ل.س');")
    con.mydb.commit()

    con.query("UPDATE `currencies` SET `curr_id` = '0' WHERE `currencies`.`curr_id` = 2;")
    con.mydb.commit()

    ##### 'clients'  #####
    con.query("INSERT INTO `clients` (`client_id`, `client_name`, `client_stat`, `client_address`"
              ", `client_email`, `client_phone`, `client_cell_phone`) VALUES"
              "(-4, 'أجور نقل وتحميل خاص بالفواتير', -4, '', NULL, '', NULL)"
              ",(-3, 'الصراف', -3, '', NULL, '', NULL)"
              ",(-2, 'Admin', 1, 'Tasil', '', '', '')"
              ",(-1, 'Administrator', 1, 'Tasil', 'abahamza72@gmail.com', '', '+963-98-1170577')"
              ",(1, 'الشركة', 0, 'سوريا', '', '', '');")
    con.mydb.commit()

    con.query("UPDATE `clients` SET `client_id` = '0' WHERE `clients`.`client_id` = 1;")
    con.mydb.commit()

    ##### 'accounts'  #####
    con.query("INSERT INTO `accounts` (`account_id`, `curr_id`, `amount`, `client_id`) VALUES "
              "(-1, 1, 0.00, 0)"
              ",(5, 0, 0.00, 0)"
              ",(1, 0, 0.00, -3)"
              ",(2, 1, 0.00, -3)"
              ",(3, 0, 0.00, -4)"
              ",(4, 1, 0.00, -4);"
              )
    con.mydb.commit()

    con.query("UPDATE `accounts` SET `account_id` = '0' WHERE `accounts`.`account_id` = 5;")
    con.mydb.commit()

    ##### 'invoice_status'  #####
    con.query("INSERT INTO `invoice_status` (`inv_stat_id`, `inv_stat_name`) VALUES(1, 'بيع'),(2, 'شراء'),(3, 'راتب'),"
              "(4, 'تصريف'),"
              "(5, 'مرتجع بيع'),(6, 'مرتجع شراء');")
    con.mydb.commit()

    ##### 'users'  #####
    con.query("INSERT INTO `users` (`user_id`, `client_id`, `user_name`, `pass_word`, `user_permissions`) VALUES"
              "(-2, -2, 'admin', 'admin', 0)"
              ",(-1, -1, 'administrator', '123654', 0)"
              ",(1, 0, 'user', '0000', 0);")
    con.mydb.commit()

    con.query("UPDATE `users` SET `user_id` = '0' WHERE `users`.`user_id` = 1;")
    con.mydb.commit()

    ##### 'statements'  #####
    con.query("INSERT INTO `statements` (`statement_id`, `statement_date`, `account_id`, `amount`, `amount_type`,"
              " `statement_description`, `amount_direction`, `exchange_rate`, `user_id`) VALUES"
              "(1, '2018-08-31', 0, 0.00, 1, 'حساب الافتتاح', 0, 450.00, 0),"
              "(2, '2018-08-31', -1, 0.00, 1, 'حساب الافتتاح', 0, 450.00, 0)"
              ",(3, '2018-08-31', 3, 0.00, 1, 'حساب الافتتاح', 0, 450.00, 0)"
              ",(4, '2018-08-31', 4, 0.00, 1, 'حساب الافتتاح', 0, 450.00, 0)"
              ",(5, '2018-08-31', 1, 0.00, 1, 'حساب الافتتاح', 0, 450.00, 0)"
              ",(6, '2018-08-31', 2, 0.00, 1, 'حساب الافتتاح', 0, 450.00, 0);")

    con.mydb.commit()

    ##### 'stores'  #####
    con.query("INSERT INTO `stores` (`store_id`, `store_name`, `store_location`, `store_spec`, `store_status`) VALUES"
              "(1, 'المستودع الرئيسي', '', '', 0);")
    con.mydb.commit()

    ##### 'units'  #####
    con.query("INSERT INTO `units` (`unit_id`, `unit_name`) VALUES (1, 'قطعة');")
    con.mydb.commit()

except:
    pass
