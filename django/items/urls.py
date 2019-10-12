from django.urls import path

from items import views

urlpatterns = [
    path('', views.items, name='items'),
    path('add', views.additem, name='additem'),
    path('edit/<int:id>', views.edititem, name='edititem'),
    
]