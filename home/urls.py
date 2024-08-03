from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('services',views.services,name="services"),
    path("contact",views.contact,name="contact"),
    path("traditional",views.traditional,name="traditional"),
    path("cultural",views.cultural,name="cultural"),
    path("ocassional",views.ocassional,name="ocassional"),
    path("address",views.address,name="address"),
    path("payment",views.payment,name="payment"),
    path("successful",views.successful,name="successful"),
    path("status",views.status,name="status"),
    path("contactsuccess",views.contactsuccess,name="contactsuccess"),
]