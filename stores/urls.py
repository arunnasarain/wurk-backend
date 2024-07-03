from django.urls import path
from .views import get_one_store

urlpatterns = [
    path('get_one_store/', get_one_store, name='get_one_store'),
]
