from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view ,name='home'),
    path('create/', views.create_url_view ,name='create'),
    path('redirect/<str:url>/', views.redirect_view ,name='redirect'),
]
