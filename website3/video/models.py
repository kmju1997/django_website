from django.db import models

# Create your models here.
class Video(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Movie(models.Model):
    category = models.ForeignKey(Video, on_delete=models.CASCADE)
    movie_title=models.CharField(max_length=200)
    director=models.CharField(max_length=250)
    genre=models.CharField(max_length=100)
    file_type = models.CharField(max_length= 10)

    def __str__(self):
        return self.movie_title

class Drama(models.Model):
    category = models.ForeignKey(Video, on_delete= models.CASCADE)
    drama_title = models.CharField(max_length=200)
    writer=models.CharField(max_length=250)
    genre=models.CharField(max_length=100)
    file_type = models.CharField(max_length=10)

    def __str__(self):
        return self.drama_title