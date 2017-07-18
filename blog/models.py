from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=32 , default='Title')
    category = models.CharField(max_length=50,blank=True)
    content = models.TextField(null=True)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-date_time']

    pass