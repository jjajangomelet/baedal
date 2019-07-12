from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('form/', views.form, name='form'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('oauth/', include('allauth.urls')),
]