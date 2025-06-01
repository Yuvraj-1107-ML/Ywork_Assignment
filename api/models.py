from django.db import models 

class Item(models.Model):
    username = models.CharField(max_length=150)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
