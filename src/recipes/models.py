from django.db import models

# Create your models here.
class Recipe(models.Model):
    name= models.CharField(max_length=50)
    ingredients= models.TextField(max_length=255, help_text='Enter the ingredients, seperated by commas')
    cooking_time= models.IntegerField(help_text='Enter the cooking time in minutes')
    difficulty= None

    def __str__(self):
        return f"Recipe Name: {self.name}"
    