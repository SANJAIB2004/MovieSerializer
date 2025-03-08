from django.db import models


# Create your models here.

class Moviedata(models.Model):

    def __str__(self):
        return self.title
    title = models.CharField(max_length=100)
    duration = models.FloatField()
    rating = models.FloatField()
    img = models.ImageField(upload_to='Images/',default='Images/None/Noimg.jpg')
    typ = models.CharField(max_length=100, default='action')

