from django.urls import path, re_path
from .views import *

app_name = "read"
urlpatterns = [
    path('<str:npm>', read, name='read'),
]
