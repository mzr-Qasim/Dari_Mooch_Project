from django.shortcuts import render
def homePage(request):
    Ice_Blast_Section_Data= {
        "IceBlast":[{"id":1,"title":"Ice Blast Bundle","price":1399.00,"description":"K","image":"static/images/1.webp"},{"id":2,"title":"Ice Blast Face Wash","price":799.00,"description":"S","image":"static/images/2.webp"},{"id":3,"title":"Ice Blast Body Wash","price":699.00,"description":"great","image":"static/images/3.webp"}]
    }
    return render(request, 'index.html', Ice_Blast_Section_Data)



def aboutPage(request):
    return render(request, 'about.html')

def loginPage(request):
    return render(request, 'login.html')
