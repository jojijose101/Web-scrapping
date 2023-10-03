from django.db import models

# Create your models here.
class Link(models.Model):
    address = models.CharField(max_length=500,null=True,blank=True)
    strname = models.CharField(max_length=500,null=True,blank=True)
    def __str__(self):
        return '{}'.format(self.strname)