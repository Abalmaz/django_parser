from ...parser_project.celery import app
from ...shop_parser.models import Product
import json

@app.task
def save_to_db(item):
    product = json.loads(item)
    Product.objects.get_or_create(
        name=product['name'],
        brand=product['brand'],
        price=product['price'],
        description=product['description'],
        currency=product['currency'],
        size=product['size'],
        color=product['color'],
        image=product['image']
    )