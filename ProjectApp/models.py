from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categorys'

    # 2 - tis function is trigerd, and it call "product_by_category" url path name and pass catogory url as argument (go to urls.py)
    def get_url(self):
        return reverse('projectApp:product_by_category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)
    
    
class Movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250,unique=True)
    image_1 = models.ImageField(upload_to='product')
    description = models.TextField(blank=True)
    date = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=350)
    #category = models.ForeignKey(Category,on_delete=models.CASCADE)
    actors_1 = models.TextField(max_length=350)
    actors_2 = models.TextField(max_length=350, blank=True)
    actors_3 = models.TextField(max_length=350, blank=True)
    link = models.CharField(max_length=450)

    created = models.DateTimeField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)
    

class MovieReview(models.Model):
    user_name = models.CharField(max_length=255)
    movie_name = models.CharField(max_length=255)
    review_text = models.TextField()
    rating = models.IntegerField(choices=((1, '⭐'), (2, '⭐⭐'), (3, '⭐⭐⭐'), (4, '⭐⭐⭐⭐'), (5, '⭐⭐⭐⭐⭐')))
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.movie_name} - {self.rating}"
    


