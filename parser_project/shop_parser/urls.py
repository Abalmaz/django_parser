from django.urls import path
from .views import index, results

urlpatterns = [
    path('', index),
    path('results', results, name='parser_results'),
]