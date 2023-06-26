from django.shortcuts import render

# Create your views here.
def home_teleco(request):
    return render(request, 'teleco/home.html')