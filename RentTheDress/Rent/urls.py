from django.conf.urls import url
from . import views

app_name = 'RentTheDress'

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^inventory$', views.inventory, name='inventory'),
    url(r'^about$', views.about, name='about'),

]