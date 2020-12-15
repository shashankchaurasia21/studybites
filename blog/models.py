from django.db import models

# Create your models here.
class post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    slug=models.CharField(max_length=130)
    content=models.TextField()
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return  self.title + ' by ' + self.author