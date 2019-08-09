from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('account/', include('allauth.urls')),
    path('account_create/', views.account_create, name='account_create'),
    path('signup/', views.signup, name="signup"),
    path('password/reset/', views.password_reset, name="password_reset"),
]