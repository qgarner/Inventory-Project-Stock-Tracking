from django.shortcuts import render
from .models import *

# Create your views here.

def items_list(request):
    list_of_items = Item.objects.all()
    items_list = list_of_items
    context = {"items_list": items_list}
    return render(request, "StockTracking/items_list.html", context)