from django.contrib import admin
from django.urls import path
from House_price import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name="Home"),
    path('price',views.result,name="result")
]
