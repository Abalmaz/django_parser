from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

import json


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parser_project.settings')

app = Celery('parser_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task
def save_to_db(item):
    from shop_parser.models import Product
    product = json.loads(item)
    Product.objects.get_or_create(
        name=product['name'],
        # brand=product['brand'],
        # price=product['price'],
        # description=product['description'],
        # currency=product['currency'],
        # size=product['size'],
        # color=product['color'],
        # image=product['image']
    )

