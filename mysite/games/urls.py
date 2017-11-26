from django.conf.urls import url

from . import views

app_name = 'games'
urlpatterns = [
    # ex: /games/
    url(r'^$', views.index, name='index'),
]