from django.db import models

# Create your models here.
class JobOrder(models.Model):
    isbn = models.CharField(verbose_name='ISBN', max_length=13, unique=True)
    title = models.CharField(verbose_name='书名', max_length=150, unique=True)
