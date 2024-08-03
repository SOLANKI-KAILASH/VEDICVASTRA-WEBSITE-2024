from django.contrib import admin
from .models import ContactModel,AddressModel,PaymentModel

class  showcontact(admin.ModelAdmin):
    list_display=["firstname","lastname","email","phone","message"]

class showaddress(admin.ModelAdmin):
    list_display=["name","email","address","city","state","zip"]

class showpayment(admin.ModelAdmin):
    list_display=["name","number","expiration","cvv"]

admin.site.register(ContactModel,showcontact)
admin.site.register(AddressModel,showaddress)
admin.site.register(PaymentModel,showpayment)
#kailash 
#pwd== 1577