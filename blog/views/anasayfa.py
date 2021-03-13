from django.shortcuts import render



def anasayfa(request):
    context = {
        'isim':'Ugur hmz'
    }
    return render(request,"pages/anasayfa.html", context=context)