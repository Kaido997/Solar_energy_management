from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('logout', views.log_out, name='log_out'),
    path('new', views.getNewData, name='getNewData'),
    path('secure', views.secure, name='secure'),
]