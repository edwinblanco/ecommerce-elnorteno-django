from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
"""class CategoriaTeleco(models.Model):
    nombre = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, unique=True)
    imagen = models.ImageField(upload_to="imagenes/categorias", blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Categoría Producto Teleco"
        verbose_name_plural = ("Categorías Productos Telecomunicacioens")
        ordering = ['nombre']"""
    
class MarcaProductoTeleco(models.Model):
    nombre = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to="imagenes/categorias", blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Marca Producto Teleco"
        verbose_name_plural = ("Marcas Productos Telecomunicaciones")
        
class CondicionProductoTeleco(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Condición Producto Teleco"
        verbose_name_plural = ("Condiciones Productos Telecomunicaciones")
        
class FormaEnvioProductoTeleco(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Forma Envío Producto Teleco"
        verbose_name_plural = ("Formas Envío Productos Telecomunicaciones")
        
class TipoGarantiaProductoTeleco(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Tipo Garatía Producto Teleco"
        verbose_name_plural = ("Tipos Garantía Productos Telecomunicaciones")
        
class TipoConexRouterTeleco(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Tipo Conexión Swith Teleco"
        verbose_name_plural = ("Tipos Conexiones Swithes Telecomunicaciones")
        
class ProductoTeleco(models.Model):
    nombre = models.CharField(max_length=250)
    sku = models.CharField(max_length=250, unique=True)
    stock = models.IntegerField()
    precio = models.IntegerField()
    codigo_universal = models.CharField(max_length=20, unique=True)
    descripcion = models.CharField(max_length=1000, blank=True)
    condicion = models.ForeignKey(CondicionProductoTeleco, on_delete=models.CASCADE, null=True)
    forma_envio = models.ForeignKey(FormaEnvioProductoTeleco, on_delete=models.CASCADE, null=True)
    retiro_en_persona = models.BooleanField(default=False)
    tipo_garantia = models.ForeignKey(TipoGarantiaProductoTeleco, on_delete=models.CASCADE, null=True)
    tiempo_garantia = models.IntegerField()
    unidad_garantia = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='imagenes/productos_teleco', blank=True)
    marca = models.ForeignKey(MarcaProductoTeleco, on_delete=models.CASCADE, null=True)
    modelo = models.CharField(max_length=250)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True

class ProductoRouterTeleco(ProductoTeleco):
    unidades_x_paquete = models.IntegerField()
    color = models.CharField(max_length=20)
    version = models.CharField(max_length=20)
    voltaje = models.CharField(max_length=100)
    con_conexion_poe = models.BooleanField(default=False)
    funciones = models.CharField(max_length=2000)
    tipo_conexion = models.ForeignKey(TipoConexRouterTeleco, on_delete=models.CASCADE, null=True)
    velocidad_inalambrica = models.IntegerField()
    unidad_velocidad = models.CharField(max_length=20)
    frecuencias = models.CharField(max_length=200)
    tipo_frecuencia = models.CharField(max_length=100)
    cant_antenas_ext = models.IntegerField()
    cant_antenas_int = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Producto Router Teleco"
        verbose_name_plural = ("Productos Router Telecomunicaciones")
    
class ProductoSwitchTeleco(ProductoTeleco):
    puntos_incluidos = models.IntegerField()
    serie = models.CharField(max_length=20)
    tipo_telecomunicacion = models.CharField(max_length=50)
    capacidad_telecomunicacion = models.IntegerField()
    unidad_capacidad_teleco = models.IntegerField()
    es_gestionable = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Producto Switch Teleco"
        verbose_name_plural = ("Productos Switches Telecomunicaciones")
        
class ProductoOtroTeleco(ProductoTeleco):
    ficha_tecnica = RichTextField()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Otro Producto Teleco"
        verbose_name_plural = ("Otros Productos Telecomunicaciones")