from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from datetime import timedelta
# Create your models here.
class Customer(models.Model):
    c_id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=20,)
    last_name=models.CharField(max_length=20)
    phone_no=models.CharField(max_length=10,unique=True)
    Address=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    date_joined=models.DateTimeField(_('date joined'), default=timezone.now)
    TYPE = [("NORMAL", "Normal",), ("SILVER", "silver",), ("GOLD", "gold",)]
    tyype=models.CharField(choices=TYPE,default="Normal",max_length=20)

    def __str__(self):
        return str(self.c_id) + " | " +self.first_name +" | "+self.last_name+self.tyype

    class Meta:
        db_table = "Customer"

class Delivery_person(models.Model):
    IDEN_TYPE=[("AADHAR", "aahdhar"),("PAN", "pan")]
    VEH_TYPE=[("BIKE","bike"),("GEARLESS","gearless")]
    d_id=models.IntegerField(primary_key=True)
    del_first_name=models.CharField(max_length=20)
    del_last_name=models.CharField(max_length=20)
    del_phone_no=models.CharField(max_length=10,unique=True)
    del_Address=models.CharField(max_length=100)
    del_email=models.EmailField(unique=True)
    del_date_joined=models.DateTimeField(_('date joined'), default=timezone.now)
    identity_type=models.CharField(choices=IDEN_TYPE,default="aadhar",max_length=20)
    license_no=models.CharField(max_length=6,unique=True)
    vehicle_no=models.CharField(max_length=10,unique=True)
    vehilcle_type=models.CharField(choices=VEH_TYPE,max_length=20)

    def __str__(self):
        return self.identity_type

    class Meta:
        db_table = "Delivery_person"

class Restaurant(models.Model):
    RES_TYPE= [("CHINESE","chinese"),("SOUTHINDIAN","southindian"),("NORTHINDIAN","northindian"),("BAKERY","bakery"),("SNACKS","snacks")]
    ret_id = models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    res_type=models.CharField(choices=RES_TYPE,max_length=20)
    phone_no=models.CharField(max_length=10,unique=True)

    def __str__(self):
        return str(self.ret_id)+ " | "+ self.name

    class Meta:
        db_table= "Restaurant"

class Menu(models.Model):
    menu_id=models.IntegerField(primary_key=True)
    title = models.CharField("Title", max_length=255)
    description = models.TextField("Description")
    restaurant = models.ForeignKey(Restaurant, related_name="Menu",on_delete=models.CASCADE)

    def __str__(self):
        return str(self.menu_id)+" | "+ self.title

    class Meta:
        db_table= "Menu"

class Meal(models.Model):
    meal_id=models.IntegerField(primary_key=True)
    menu = models.ForeignKey(Menu, related_name="meal",on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField("Title", max_length=255)
    price = models.FloatField("Price")

    def __str__(self):
        return self.title

    class Meta:
        db_table= "Meal"

def order_time():
    return timezone.now() + timedelta(hours=1)

class Order(models.Model):
    CANCELLED_BY_CLIENT = "cancelled_by_client"
    NEW = "new"
    ORDER_STATUS = [(NEW, "New",), ("finalized", "Finalized",), ("rejected", "Rejected",),
                    (CANCELLED_BY_CLIENT, "Cancelled by client",),("preparing","preparing")]
    order_id=models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    delivery_person=models.ForeignKey(Delivery_person,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    order_time = models.DateTimeField(default=order_time)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=ORDER_STATUS, default="new", max_length=100)

    def __str__(self):
        return str(self.order_id) +" | "+self.status

    class Meta:
        db_table= "Order"

class Item_Quantity(models.Model):
    q_id=models.IntegerField(primary_key=True)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    meal=models.ForeignKey(Meal,on_delete=models.CASCADE)
    quantity=models.IntegerField()

    def __str__(self):
        return str(self.q_id)

    class Meta:
        db_table= "Item_Quantity"


class Payment(models.Model):
    PAY_TYPE=[("cash","cash"),("Credit card","Credit card"),("Debit card","Debit Card"),("wallet","wallet")]
    order=models.OneToOneField(Order,on_delete=models.CASCADE)
    tran_id=models.IntegerField()
    Amount= models.FloatField()
    Date=models.DateTimeField(default=timezone.now)
    Mode=models.CharField(choices=PAY_TYPE,max_length=20,default="cash")

    def __str__(self):
        return str(self.tran_id)

    class Meta:
        db_table="Payment"