from django.db import models

# Create your models here.
class Food(models.Model):
	main_dish = models.TextField(default='')
	side_dish = models.TextField(default='')
