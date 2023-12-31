from pyexpat import model
from turtle import title 
from django.db import models
# Create your models here.
from django.urls import reverse
from django.utils import timezone

class Post(models.Model):

    title = models.CharField(max_length=200,null = True)

    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        null = True,
    )

    body = models.TextField(default = timezone.now)


    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk":self.pk})
    