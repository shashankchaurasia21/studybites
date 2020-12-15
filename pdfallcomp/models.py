from django.db import models

# Create your models here.
class Pdfallcomp(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    author=models.CharField(max_length=100)
    upload = models.FileField(upload_to='media/file/')
    timeStamp = models.DateTimeField(blank=True)
    def __str__(self):
        return  self.title + ' by ' + self.author