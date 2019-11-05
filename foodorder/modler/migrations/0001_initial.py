# Generated by Django 2.1.7 on 2019-10-22 01:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import modler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('c_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone_no', models.CharField(max_length=10, unique=True)),
                ('Address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('tyype', models.CharField(choices=[('NORMAL', 'Normal'), ('SILVER', 'silver'), ('GOLD', 'gold')], default='Normal', max_length=20)),
            ],
            options={
                'db_table': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='Delivery_person',
            fields=[
                ('d_id', models.IntegerField(primary_key=True, serialize=False)),
                ('del_first_name', models.CharField(max_length=20)),
                ('del_last_name', models.CharField(max_length=20)),
                ('del_phone_no', models.CharField(max_length=10, unique=True)),
                ('del_Address', models.CharField(max_length=100)),
                ('del_email', models.EmailField(max_length=254, unique=True)),
                ('del_date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('identity_type', models.CharField(choices=[('AADHAR', 'aahdhar'), ('PAN', 'pan')], default='aadhar', max_length=20)),
                ('license_no', models.CharField(max_length=6, unique=True)),
                ('vehicle_no', models.CharField(max_length=10, unique=True)),
                ('vehilcle_type', models.CharField(choices=[('BIKE', 'bike'), ('GEARLESS', 'gearless')], max_length=20)),
            ],
            options={
                'db_table': 'Delivery_person',
            },
        ),
        migrations.CreateModel(
            name='Item_Quantity',
            fields=[
                ('q_id', models.IntegerField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
            ],
            options={
                'db_table': 'Item_Quantity',
            },
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('meal_id', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('price', models.FloatField(verbose_name='Price')),
            ],
            options={
                'db_table': 'Meal',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'db_table': 'Menu',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('order_time', models.DateTimeField(default=modler.models.order_time)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('new', 'New'), ('finalized', 'Finalized'), ('rejected', 'Rejected'), ('cancelled_by_client', 'Cancelled by client'), ('preparing', 'preparing')], default='new', max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modler.Customer')),
                ('delivery_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modler.Delivery_person')),
            ],
            options={
                'db_table': 'Order',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tran_id', models.IntegerField()),
                ('Amount', models.FloatField()),
                ('Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Mode', models.CharField(choices=[('cash', 'cash'), ('Credit card', 'Credit card'), ('Debit card', 'Debit Card'), ('wallet', 'wallet')], default='cash', max_length=20)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='modler.Order')),
            ],
            options={
                'db_table': 'Payment',
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('ret_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('res_type', models.CharField(choices=[('CHINESE', 'chinese'), ('SOUTHINDIAN', 'southindian'), ('NORTHINDIAN', 'northindian'), ('BAKERY', 'bakery'), ('SNACKS', 'snacks')], max_length=20)),
                ('phone_no', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'db_table': 'Restaurant',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modler.Restaurant'),
        ),
        migrations.AddField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Menu', to='modler.Restaurant'),
        ),
        migrations.AddField(
            model_name='meal',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal', to='modler.Menu'),
        ),
        migrations.AddField(
            model_name='item_quantity',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modler.Meal'),
        ),
        migrations.AddField(
            model_name='item_quantity',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modler.Order'),
        ),
    ]