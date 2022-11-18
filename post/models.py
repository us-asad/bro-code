from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Post(models.Model):
	title = models.CharField(max_length=250)
	body = models.TextField()
	thumbnail = models.ImageField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.title)

	
	def get_absolute_url(self):
		return reverse('post:postDetail', kwargs={
		'id': self.id
		})
