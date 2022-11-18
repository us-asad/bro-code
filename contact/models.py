from django.db import models


class Contact(models.Model):
	name = models.CharField(max_length=150)
	email = models.EmailField()
	phone_num = models.IntegerField()
	body  = models.TextField()

	def __str__(self):
		return str(f'{self.id} {self.name}')



