from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = "APP"
urlpatterns = [
    path("", views.index, name="index"),
    path("index.html", views.index, name="index2"),
    path("services.html", views.services, name="services"),
    path("blog-home.html", views.BlogListView.as_view(), name="blog"),
    path("team.html", views.team, name="team"),
    path("contact.html", views.contact, name="contact"),
    path("details/<slug>", views.BlogDetailView.as_view(), name="details"),




]
