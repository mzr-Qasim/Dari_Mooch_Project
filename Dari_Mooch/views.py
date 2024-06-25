from django.shortcuts import render
from Dari_Mooch_Products.models import Products
from Dari_Mooch_Carousels.models import Carousels

def homePage(request):
    Products_Data = Products.objects.all()
    Carousels_Data = Carousels.objects.all()
    Data= {
        "products": Products_Data,
        "carousels":Carousels_Data
    }
    return render(request, 'index.html', Data)



def aboutPage(request):
    return render(request, 'about.html')

def loginPage(request):
    return render(request, 'login.html')
