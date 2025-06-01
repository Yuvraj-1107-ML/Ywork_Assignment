from django.urls import path  
from . import views

urlpatterns = [
    path('oauth/', views.oauth_login),
    path('items/', views.add_item),
    path('items/list/', views.get_items),
]
