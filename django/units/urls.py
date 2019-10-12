from django.urls import path

from units import views

urlpatterns = [
    path('', views.units, name='units'),
    path('add', views.addunit, name='addunit'),
    path('edit/<int:id>', views.editunit, name='editunit'),
    
]