from django.urls import path
from estatico import views
from .views import http_response_view


urlpatterns = [
    path('', views.index, name='index'),
    path('simple/', http_response_view), 
]