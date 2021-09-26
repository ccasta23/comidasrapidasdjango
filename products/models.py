from django.db import models

# Create your models here.
class Product(models.Model):
    """Clase producto con todos sus atributos"""
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField( blank=True )
    value = models.PositiveIntegerField()
    
    image = models.CharField(max_length=255, blank=True)

    active = models.BooleanField(default=True)

    ## Campos de auditoria
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name