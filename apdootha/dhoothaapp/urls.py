from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', Registration.as_view(), name='register'),
    path('addmem/', AddMember.as_view(), name='addmem'),
]
