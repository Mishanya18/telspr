from django.urls import path

from telspr.views import index


urlpatterns = [
    path('', index),
]
