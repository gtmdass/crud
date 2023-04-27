from django.core.management.base import BaseCommand, CommandError

from crudapp.models import Category, Product

import requests, traceback

class Command(BaseCommand):
    help = "Get or create Categories and Products from third party api."

    def handle(self, *args, **options):
        try:
            url = 'https://fakestoreapi.com/products'
            response  = requests.get(url)
            for item in response.json():
                cat, cat_created = Category.objects.get_or_create(title=item['category'])
                prod, prod_created = Product.objects.get_or_create(title=item['title'])
                prod.description = item['description']
                prod.price = item['price']
                prod.image = item['image']
                prod.category = Category.objects.get(title=item['category'])
                prod.save()
                print("Getting Products -- ", prod)
        except:
            print(traceback.print_exc())