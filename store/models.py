from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
# Class Catégorie
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    class Meta:
        verbose_name_plural = 'categories'
    
    def get_absolute_url(self):
        # store: nom de l'app definir dans urls et product_detail:son name dans urls.py
        # args Recupere son slug
        return reverse('store:category_list', args=[self.slug])
    
    def __str__(self):
        return self.name
    
    
# Class Produit
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)
        
    def get_absolute_url(self):
        # store: nom de l'app definir dans urls et product_detail:son name dans urls.py
        # args Recupere son slug
        return reverse('store:product_detail', args=[self.slug])
    
        
    def __str__(self):
        return self.title
    