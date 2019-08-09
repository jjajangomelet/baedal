from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'orders'

urlpatterns = [
    path('', views.cover, name="cover"),
    path('index/', views.index, name="index"),
    path('matching_list/', views.matching_list, name="matching_list"),
    path('new_host/', views.new_host, name="new_host"),
    path('matching_detail/<int:matching_id>', views.matching_detail, name="matching_detail"),
    path('matching_participant/', views.new_participant, name ="new_participant"),
    path('create_order/', views.create_order, name="create_order"),
    path('matching_create/', views.matching_create, name="matching_create"),

    # path('create/', views.create, name="create"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)