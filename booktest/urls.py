from django.conf.urls import url
from booktest import views


urlpatterns = [
    url(r'^set_sessions$', views.set_sessions),
    url(r'^get_sessions$', views.get_sessions),
]


