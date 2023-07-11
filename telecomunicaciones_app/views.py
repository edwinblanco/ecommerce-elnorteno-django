from django.shortcuts import render
from telecomunicaciones_app.models import MarcaProductoTeleco

# Create your views here.
def home_teleco(request):
    marcas = MarcaProductoTeleco.objects.all()
    
    return render(request, 'teleco/home.html', {'marcas':marcas})