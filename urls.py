from django.conf.urls import url
from . import views

app_name = "cv"

urlpatterns = [
    url(r'^$', views.About, name='about'),
    url(r'^cv$', views.CV, name='cv'),

]
