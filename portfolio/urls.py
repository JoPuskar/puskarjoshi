from urllib.parse import urlparse
from django.urls import path
from .views import portfolio

app_name = 'portfolio'

urlpatterns = [
    path('', portfolio, name='portfolio'),
]