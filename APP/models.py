from django.db import models
from django.shortcuts import reverse
# Create your models here.
class Post(models.Model):
    title= models.TextField()
    body= models.TextField()
    img= models.ImageField()
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse("APP:details", kwargs={
            'slug': self.slug
        })
