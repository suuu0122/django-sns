from django.db import models



class Tweet(models.Model):
    title       = models.CharField(max_length=100)
    content     = models.TextField()
    contributor = models.TextField()
    sns_image   = models.ImageField(upload_to='')
    good        = models.IntegerField()
    read        = models.IntegerField()
    read_text   = models.TextField()