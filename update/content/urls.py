from django.urls import path, re_path
from .views import *

app_name = "update"
urlpatterns = [
    path('', update, name='update'),
]
