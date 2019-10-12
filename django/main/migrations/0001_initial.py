# Generated by Django 2.2.2 on 2019-09-11 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curr', models.SmallIntegerField(choices=[(0, 'دولار أمريكي'), (1, 'ليرة سورية')])),
                ('amount', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=70)),
                ('client_stat', models.SmallIntegerField(choices=[(-4, 'نقل وتحميل'), (-3, 'صراف'), (-2, 'مساهم'), (-1, 'نثريات'), (0, 'المالك'), (1, 'موظف'), (2, 'مورد'), (3, 'زبون')])),
                ('client_address', models.TextField(null=True)),
                ('client_email', models.EmailField(max_length=70, null=True)),
                ('client_phone', models.CharField(max_length=16, null=True)),
                ('client_cell_phone', models.CharField(max_length=16, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_date', models.DateField()),
                ('cash', models.FloatField()),
                ('stock', models.FloatField()),
                ('debtors', models.FloatField()),
                ('fund', models.FloatField()),
                ('creditors', models.FloatField()),
                ('profit', models.FloatField()),
                ('notes', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_date', models.DateField()),
                ('inv_stat', models.SmallIntegerField(choices=[(1, 'بيع'), (2, 'شراء'), (3, 'راتب'), (4, 'تصريف'), (5, 'مرتجع بيع'), (6, 'مرتجع شراء')])),
                ('payment_date', models.DateField(null=True)),
                ('discount', models.FloatField(null=True)),
                ('ref_number', models.CharField(max_length=25)),
                ('delivery', models.FloatField(null=True)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Accounts')),
            ],
        ),
        migrations.CreateModel(
            name='Statements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement_date', models.DateField(null=True)),
                ('amount', models.FloatField()),
                ('amount_type', models.SmallIntegerField(choices=[(0, 'Money'), (1, 'Goods')])),
                ('statement_description', models.TextField()),
                ('amount_direction', models.SmallIntegerField(choices=[(0, 'Income'), (1, 'Outlay')])),
                ('exchange_rate', models.FloatField()),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Accounts')),
            ],
        ),
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('location', models.CharField(max_length=50)),
                ('specs', models.TextField()),
                ('status', models.SmallIntegerField(choices=[(0, 'نشط'), (2, 'غير نشط')])),
            ],
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=25)),
                ('pass_word', models.CharField(max_length=50)),
                ('user_permissions', models.IntegerField()),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Clients')),
            ],
        ),
        migrations.CreateModel(
            name='Statements_Invoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Invoices')),
                ('statement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Statements')),
            ],
        ),
        migrations.AddField(
            model_name='statements',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Users'),
        ),
        migrations.CreateModel(
            name='Operations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_date', models.DateTimeField()),
                ('operation_description', models.TextField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('specs', models.TextField()),
                ('minimum_quantity', models.FloatField()),
                ('cost', models.FloatField()),
                ('minimum_price', models.FloatField()),
                ('normal_price', models.FloatField()),
                ('status', models.BooleanField(choices=[(False, 'صنف متداول'), (True, 'صنف غير متداول')])),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Units')),
            ],
        ),
        migrations.AddField(
            model_name='invoices',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Stores'),
        ),
        migrations.AddField(
            model_name='invoices',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Users'),
        ),
        migrations.CreateModel(
            name='Inv_Quantities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_price', models.FloatField()),
                ('item_cost', models.FloatField(default=0.0)),
                ('quantity', models.FloatField()),
                ('discount_for_item', models.FloatField()),
                ('inv', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Invoices')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Items')),
            ],
        ),
        migrations.AddField(
            model_name='accounts',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Clients'),
        ),
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=0.0)),
                ('last_in_date', models.DateField(null=True)),
                ('last_out_date', models.DateField(null=True)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Items')),
                ('store', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Stores')),
            ],
            options={
                'unique_together': {('store', 'item')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='accounts',
            unique_together={('curr', 'client')},
        ),
    ]
