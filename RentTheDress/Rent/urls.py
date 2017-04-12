from django.conf.urls import url
from . import views

app_name = 'RentTheDress'

urlpatterns = [
    # These direct the user to where they need to go by using the view functions EX: views.home
    url(r'^$', views.home, name='home'),
    url(r'^inventory$', views.inventory, name='inventory'),
    url(r'^about$', views.about, name='about'),
    url(r'^rent/(?P<id>[0-9]+)/$', views.renting, name='rent'),
    url(r'^return/(?P<id>[0-9]+)/$', views.returning, name='return')
]