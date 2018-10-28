from django.urls import path

from .views import index

app_name = 'assets'

urlpatterns = [
    path('index/', index, name='index')
]
