from django.conf.urls import url
from bucket import views


urlpatterns = [
    url(r'^$', views.index)
]