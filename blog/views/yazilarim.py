from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



@login_required(login_url='/') #kayıtlı olmayan kullanıcı için anasayfaya yönlendirir.
def yazilarim(request):     #bana giriş yapmış kullanıcının yazıları lazım.
    yazilar = request.user.yazilar.order_by('-id') # #related_name ile yazarın bütün yazılarıan eriştik
    sayfa = request.GET.get('sayfa')
    paginator =Paginator(yazilar,2)


    context = {
        'yazilar':paginator.get_page(sayfa),
    }

    return render(request,"pages/yazilarim.html", context=context)


