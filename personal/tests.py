from django.test import TestCase
from .models import Image,Location,Categories


# Create your tests here.

class LocationTestClass(TestCase):
    '''Test class to test location class'''
    def setUp(self):
        '''Function to prepare for every test case'''
        self.Eldoret = Location(location = 'Eldoret')

    def tearDown(self):
        '''Function to clean up after every test case'''
        Location.objects.all().delete()

    def test_instance(self):
        '''Test if test_location is an instance of location class'''
        self.assertTrue(isinstance(self.Eldoret, Location))

    def test_save_method(self):
        '''Test saving a location to database'''
        self.Eldoret.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

class CategoriesTestClass(TestCase):
    '''
    Test class to test categories class
    '''
    def setUp(self):
        '''Function to prepare for every test case'''
        self.food= Categories(categories= 'food')

    def tearDown(self):
        '''Function to clean up after every test case'''
        Categories.objects.all().delete()

    def test_instance(self):
        '''
        Test if test_category is an instance of category class
        '''
        self.assertTrue(isinstance(self.food,Categories))

    def test_save_categories(self):
        '''Test saving a category to database'''
        self.food.save_categories()
        categories = Categories.objects.all()
        self.assertTrue(len(categories) > 0)

   