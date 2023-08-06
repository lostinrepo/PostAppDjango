from django.db import models
from django.urls import reverse

class Person(models.Model):
    first_name = models.TextField(max_length=30)
    last_name = models.TextField(max_length=30)
    phone = models.BigIntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
        

        

# Create your models here.
