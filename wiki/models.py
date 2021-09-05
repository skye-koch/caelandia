from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    catName = models.CharField(max_length = 50, primary_key=True)
    # acceptable catNames currently: Location, People, DivineBeing, Thing
    
    def __str__(self):
        return f"{self.catName}" 

class Entry(models.Model):
    title = models.CharField(max_length = 1000 , unique=True, null = False)
    body = RichTextField(blank = True, null = True)
    #body = models.TextField(null = False)
    source = models.CharField(max_length = 1000,null=True, blank = True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"{self.title}" 

    

