from django.urls import path
from .views import *

urlpatterns = [
    path('', items_list, name="items_list"),
]