from django.conf.urls import url
from sampleappcount import views

urlpatterns = [
    url(r'^$', views.say_hello, name='home'),
]
