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