from django.db import models

# Create your models here.

class Carousel(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    explanation = models.TextField()
    image = models.ImageField(upload_to="carousel_images")

    def __str__(self):
        return self.name
    
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class AboutImage(models.Model):
    name = models.CharField(max_length=10)
    image = models.ImageField(upload_to='about_image')

    def __str__(self):
        return self.name
    

    
# class About(models.Model):
#     name = models.CharField(max_length=100)
#     introduction = models.CharField(max_length=100)
#     description1 = models.TextField()
#     description2 = models.TextField()
    

#     def __str__(self):
#         return self.name
    

class Feature(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Categorie(models.Model):
    name = models.CharField(max_length=50)
    courses_count = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category_image')
    
    
    def __str__(self):
        return self.name