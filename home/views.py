from django.shortcuts import render,HttpResponse

# Create your views here.
def anasayfa(request):
    if request.user.is_authenticated:
        context = {
            'isim':'yunus',
        }
    else:
        context = {
            'isim': 'misafir',
        }
    return render(request,'home.html',context)