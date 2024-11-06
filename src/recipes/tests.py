from django.test import TestCase

# Create your tests here.

from .models import Recipe

class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(
            name='Fettuccini Alfredo', 
            ingredients='water, salt, fettuccini, alfredo', 
            cooking_time=25
            )

# name tests  
    def test_recipe_name(self):
        # getting a recipe object to test
        recipe = Recipe.objects.get(id=1)
        
        # getting metadata for the 'name' field
        field_label = recipe._meta.get_field('name').verbose_name

        # comparing value of name_field with expected result
        self.assertEqual(field_label, 'name')


    def test_name_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

# ingredients tests
    def test_ingredient_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('ingredients').max_length
        self.assertEqual(max_length, 255)

# cooking_time tests
