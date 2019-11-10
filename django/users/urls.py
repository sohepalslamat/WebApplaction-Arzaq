from django.urls import path

from users import views

urlpatterns = [
    path('', views.users, name='users'),
    path('add', views.adduser, name='adduser'),
    path('login', views.login, name='login'),
    path('edit/<int:id>', views.edituser, name='edituser'),
    path('checkusername', views.checkusername, name="checkusername"),
    
    
]