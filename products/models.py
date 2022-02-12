from ctypes import sizeof
from multiprocessing.sharedctypes import SynchronizedString
from django.db import models

# Create your models here.  
class Drink(models.Model):
    category     = models.ForeignKey('Category',on_delete=models.CASCADE) 
    korean_name  = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description  = models.TextField(blank=True)
    
    class Meta:
        db_table = 'drinks'


class Category(models.Model):
    menu    = models.ForeignKey('Menu',on_delete=models.CASCADE)
    name    = models.CharField(max_length=45)
    
    
    class Meta:
        db_table = 'categories'
        
class Menu(models.Model):
    name  =  models.CharField(max_length=45)
        
    class Meta:
        db_table = 'menus'
            
class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    drink     = models.ForeignKey('Drink',on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'images'

class Allergy_drink(models.Model):
    allergy    = models.ForeignKey('Allergy',on_delete=models.CASCADE)
    drink      = models.ForeignKey('Drink',on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'allergy_drinks'
        
class Allergy(models.Model):
    name = models.CharField(max_length=45)
    
    class Meta:
        db_table = 'allergies'

class Size(models.Model):
    name             = models.CharField(max_length=45)
    size_mi          = models.CharField(max_length=45)
    size_fluid_ounce = models.CharField(max_length=45)
    
    class Meta:
        db_table = 'sizes'
        
class Nutrition(models.Model):
    one_serving_kca = models.DecimalField(decimal_places=2,max_digits=10)
    sodium_mg       = models.DecimalField(decimal_places=2,max_digits=10)
    saturated_fat_g = models.DecimalField(decimal_places=2,max_digits=10)
    sugars_g        = models.DecimalField(decimal_places=2,max_digits=10)
    protein_g       = models.DecimalField(decimal_places=2,max_digits=10)
    caffeine_mg     = models.DecimalField(decimal_places=2,max_digits=10)
    drink           = models.ForeignKey('Drink',on_delete=models.CASCADE)
    size            = models.ForeignKey('Size',on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'nutritions'
        


    

    
    