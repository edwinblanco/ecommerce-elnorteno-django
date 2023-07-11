from django.contrib import admin
from telecomunicaciones_app.models import MarcaProductoTeleco
from telecomunicaciones_app.models import CondicionProductoTeleco
from telecomunicaciones_app.models import FormaEnvioProductoTeleco
from telecomunicaciones_app.models import TipoGarantiaProductoTeleco
from telecomunicaciones_app.models import TipoConexRouterTeleco
from telecomunicaciones_app.models import ProductoOtroTeleco
from telecomunicaciones_app.models import ProductoRouterTeleco
from telecomunicaciones_app.models import ProductoSwitchTeleco

from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

class ProductoRouterTelecoResource(resources.ModelResource):
    class Meta:
        model = ProductoRouterTeleco
        
class roductoSwitchTelecoResource(resources.ModelResource):
    class Meta:
        model = ProductoSwitchTeleco
        
class ProductoOtroTelecoResource(resources.ModelResource):
    class Meta:
        model = ProductoOtroTeleco

class ProductosAdmin(ImportExportActionModelAdmin):
    export_template_name = None
    list_display = ('nombre', 'sku', 'stock','precio','codigo_universal', 'descripcion', 'condicion', 'forma_envio')
    list_display_links = ('nombre', 'sku', 'stock','precio','codigo_universal')
    #readonly_fields =  ('last_login', 'date_joined')
    ordering = ('nombre',)
    search_fields = ['nombre', 'sku', 'stock','precio','codigo_universal', 'descripcion', 'condicion', 'forma_envio']
    list_filter = ()
    filter_horizontal = ()
    fieldsets = ()

admin.site.register(MarcaProductoTeleco)
admin.site.register(CondicionProductoTeleco)
admin.site.register(FormaEnvioProductoTeleco)
admin.site.register(TipoConexRouterTeleco)
admin.site.register(TipoGarantiaProductoTeleco)
admin.site.register(ProductoSwitchTeleco, ProductosAdmin)
admin.site.register(ProductoOtroTeleco, ProductosAdmin)
admin.site.register(ProductoRouterTeleco, ProductosAdmin)

#from telecomunicaciones_app.models import CategoriaTeleco

# Register your models here.
"""class CategoriasTelecoAdmin(admin.ModelAdmin):
    prepopulated_fields = ('slug':{'name',})
    list_display = ('nombre', 'slug')
    
admin.site.register(CategoriaTeleco, CategoriasTelecoAdmin)"""