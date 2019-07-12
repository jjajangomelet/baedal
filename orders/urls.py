from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.cover, name="cover"),
    path('index/', views.index, name="index"),
    path('read/', views.read, name="read"),
    path('new_host/', views.new_host, name="new_host"),
    path('detail/', views.detail, name="detail"),
    path('new_participant/', views.new_participant, name ="new_participant"),
    path('create_order/', views.create_order, name="create_order"),
    
    # path('create/', views.create, name="create"),
    
]