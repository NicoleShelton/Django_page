from django.conf.urls import url
from . import views

app_name = 'RentTheDress'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^Inventory$', views.inventory, name='inventory'),
    url(r'^About$', views.about, name='about'),

]