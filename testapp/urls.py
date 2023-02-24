from django.contrib import admin
from django.urls import path, include
from .views import *
from .import views
urlpatterns = [
    path('',views.retrive_view, name="home"),
    path('create/',views.create_view,name="create_view"),
    path('delete/<int:id>',views.delete_view,name='delete_view'),
    path('update/<int:id>',views.update_view,name="update_view"),
    
]