from django.core.management.base import BaseCommand, CommandError
from StockTracking.models import *
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("itemlist.csv", "r") as csvfile:
            item_reader = csv.reader(csvfile, delimiter=",")
            for row in item_reader:
                item_name = item_reader[1]
                item_sku = item_reader[3]
                
                
            