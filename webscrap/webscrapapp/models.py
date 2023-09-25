from django.db import models

# Create your models here.
class ScrapLink(models.Model):
    address=models.CharField(max_length=255,null=True,blank=True)
    string_name=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.string_name