from django.db import models

# Create your models here.
class CategoriaTeleco(models.Model):
    nombre = models.CharField(max_length=250)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Categoría Producto Teleco"
        verbose_name_plural = ("Categorías Productos Telecomunicacioens")
        ordering = ['nombre']
    
class MarcaProductoTeleco(models.Model):
    nombre = models.CharField(max_length=250)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Marca Producto Teleco"
        verbose_name_plural = ("Marcas Productos Telecomunicacioens")
    
class FichaTecnica(models.Model):
    marca = periodo = models.ForeignKey(MarcaProductoTeleco, on_delete=models.CASCADE, null=True)
    modelo = models.CharField(max_length=250)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.modelo
    
    class Meta:
        verbose_name = "Ficha Técnica Producto Teleco"
        verbose_name_plural = ("Fichas Técnicas Productos Telecomunicacioens")
        
class FichaTecnica(models.Model):
    marca = periodo = models.ForeignKey(MarcaProductoTeleco, on_delete=models.CASCADE, null=True)
    modelo = models.CharField(max_length=250)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.modelo
    
    class Meta:
        verbose_name = "Ficha Técnica Producto Teleco"
        verbose_name_plural = ("Fichas Técnicas Productos Telecomunicacioens")