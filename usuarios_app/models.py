
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, nombres, apellidos, username, correo, password=None):
        if not correo:
            raise ValueError('El usuario debe tener un email')
        if not username:
            raise ValueError('El usuario debe tener un username')
         
        user = self.model(
            correo = self.normalize_email(correo),
            username = username,
            nombres = nombres,
            apellidos = apellidos,
        )
        
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, nombres, apellidos, username, correo, password):
        
        user = self.create_user(
            correo = self.normalize_email(correo),
            username = username,
            password= password,
            nombres = nombres,
            apellidos = apellidos,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True    
        user.is_superadmin = True
        user.save(using = self._db)
        return user

class Usuario(AbstractBaseUser):
    nombres = models.CharField(max_length=1000)
    apellidos = models.CharField(max_length=1000)   
    correo = models.EmailField(max_length=1000, unique=True)  
    username = models.CharField(max_length=1000, unique=True) 
    numero_celular = PhoneNumberField(blank=False)
    
    #campos de Django
    date_joined = models.DateTimeField(auto_now_add=True)   
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)   
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)   
    foto_perfil = models.ImageField(upload_to="imagenes/fotos_perfil", blank=True)
    
    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombres', 'apellidos', 'username']
    
    objects = UsuarioManager()
    
    def __str__(self):
        return self.correo+" | "+self.nombres+" "+self.apellidos
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
        
    class Meta:
        ordering = ['correo']        