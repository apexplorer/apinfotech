from django.urls import path,include
from dhoothaapp.views import *
urlpatterns = [
    
    path('',Home,name="home"),
]
