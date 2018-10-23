from django.conf.urls import url
from bucketRecord import views


urlpatterns = [
    url(r'^$', views.index)
]