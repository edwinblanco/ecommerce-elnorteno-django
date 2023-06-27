from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from usuarios_app.models import Usuario
from django.utils.html import format_html
        
class UsuarioAdmin(UserAdmin):
    list_display = ('correo', 'nombres', 'apellidos','username','ver_foto_perfil', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('correo', 'nombres', 'apellidos', 'username')
    readonly_fields =  ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    search_fields = ['correo','nombres', 'apellidos', 'username']
    list_filter = ('is_staff', 'is_active')
    filter_horizontal = ()
    fieldsets = ()
    
    def ver_foto_perfil(self, obj):
        return format_html('<a href="{}" target="_blank"><img src="{}" width="50" height="50" /></a>', obj.foto_perfil.url, obj.foto_perfil.url)

    ver_foto_perfil.short_description = 'Foto de perfil'

# Register your models here.
admin.site.register(Usuario, UsuarioAdmin)