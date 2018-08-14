from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Product

import redis

redis_server = redis.Redis(host='127.0.0.1', port=6379)

# Create your views here.


def index(request):
    if request.method == 'POST':
        redis_server.lpush('valentino:start_urls', 'https://www.valentino.com/en-us/women/pret-a-porter')
        return redirect('parser_results')


def results(ListView):
    model = Product
    template_name = 'shop_parser/results.html'

