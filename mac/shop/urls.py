
from django.urls import path
from . import views

urlpatterns = [
    path("Home",views.index,name="ShopHome"),
    path("about",views.about,name="aboutUs"),
    path("Contact",views.contact,name="Contact us"),
    path("Tracker",views.Tracker,name="Tracking status"),
    path("ProductView/<int:myid>",views.ProductView,name="search"),
    path("CheckOut",views.CheckOut,name="CheckOut")
]