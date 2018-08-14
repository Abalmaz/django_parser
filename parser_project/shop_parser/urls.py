from django.urls import path
from .views import index, results

urlpatterns = [
    path('', index),
    path('parser_results', results.as_view(), name='parser_results'),
]