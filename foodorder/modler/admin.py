from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Delivery_person)
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(Item_Quantity)
admin.site.register(Payment)