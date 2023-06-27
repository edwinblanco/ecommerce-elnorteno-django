from django.contrib import admin
from telecomunicaciones_app.models import MarcaProductoTeleco
from telecomunicaciones_app.models import CondicionProductoTeleco
from telecomunicaciones_app.models import FormaEnvioProductoTeleco
from telecomunicaciones_app.models import TipoGarantiaProductoTeleco
from telecomunicaciones_app.models import TipoConexRouterTeleco
from telecomunicaciones_app.models import ProductoOtroTeleco
from telecomunicaciones_app.models import ProductoRouterTeleco
from telecomunicaciones_app.models import ProductoSwitchTeleco

#from telecomunicaciones_app.models import CategoriaTeleco

# Register your models here.
"""class CategoriasTelecoAdmin(admin.ModelAdmin):
    prepopulated_fields = ('slug':{'name',})
    list_display = ('nombre', 'slug')
    
admin.site.register(CategoriaTeleco, CategoriasTelecoAdmin)"""

admin.site.register(MarcaProductoTeleco)
admin.site.register(CondicionProductoTeleco)
admin.site.register(FormaEnvioProductoTeleco)
admin.site.register(TipoConexRouterTeleco)
admin.site.register(TipoGarantiaProductoTeleco)
admin.site.register(ProductoSwitchTeleco)
admin.site.register(ProductoOtroTeleco)
admin.site.register(ProductoRouterTeleco)
