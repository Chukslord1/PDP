from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    return render(request, "index.html")
def services(request):
    return render(request, "services.html")
def blog(request):
    context={"blog":Post.objects.all()}
    return render(request, "blog-home.html", context)
def team(request):
    return render(request, "team.html")
def contact(request):
    return render(request, "contact.html")
