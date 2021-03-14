from django.shortcuts import render
from blog.models import YazilarModel
from django.core.paginator import Paginator #-> Paginator için

def anasayfa(request):
    yazilar = YazilarModel.objects.order_by("-id") #Enson  atılan yazıyı, en başa al.
    sayfa=request.GET.get('sayfa')
    paginator = Paginator(yazilar,2)


    context = {
        'yazilar':paginator.get_page(sayfa)
    }
    return render(request,"pages/anasayfa.html", context=context)