from django.urls import path

from items import views

urlpatterns = [
    path('add', views.additem, name='additem'),
    
    
]