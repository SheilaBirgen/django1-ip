from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=20, blank=True)
    description = models.TextField()
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    categories = models.ForeignKey("Categories", on_delete=models.CASCADE)

    @classmethod
    def search_by_category(cls, search_term):
        '''
             Method to filter images by category
        '''
        result = cls.objects.filter(categories__icontains=search_term)
        return result

    def save_image(self):
        return self.save()
  
    def delete_image(self):
        return self.delete()

class Location(models.Model):
    location = models.CharField(max_length=20)

    def save_location(self):
        return self.save()

    def delete_location(self):
        return self.delete()

    
    def __str__(self):
        return self.location

class Categories(models.Model):
    categories = models.CharField(max_length=20)

    def save_categories(self):
        return self.save()
        
    def delete_categories(self):
        return self.delete()

    def __str__(self):
        return self.categories