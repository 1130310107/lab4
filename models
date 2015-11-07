from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    country = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50,primary_key=True)
    author = models.ForeignKey(Author,blank=True,null=True)
    publisher = models.CharField(max_length=50)
    publish_date = models.DateTimeField()
    price = models.FloatField()
    def __unicode__(self):
        return self.title
