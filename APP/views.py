from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, View
# Create your views here.
def index(request):
    return render(request, "index.html")
def services(request):
    return render(request, "services.html")
def team(request):
    return render(request, "team.html")
def contact(request):
    return render(request, "contact.html")
class BlogListView(ListView):
    model = Post
    queryset = Post.objects.all()[:10]
    template_name = "blog-home.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "blog-single.html"
