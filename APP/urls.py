from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("index.html", views.index, name="index2"),
    path("services.html", views.services, name="services"),



]
