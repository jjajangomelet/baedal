from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.index, name="index"),
    path('read/', views.read, name="read"),
    path('new/', views.new, name="new"),
    path('detail/', views.detail, name="detail"),
    
    # path('create/', views.create, name="create"),
    
]