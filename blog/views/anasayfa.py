from django.shortcuts import render
from blog.models import YazilarModel
from django.core.paginator import Paginator #-> Paginator için
from django.db.models import Q # ORM içinden-> ya da işlemi için kullanılır.



def anasayfa(request):
    sorgu = request.GET.get('sorgu')
    yazilar = YazilarModel.objects.order_by("-id") #Enson  atılan yazıyı, en başa al.

    if sorgu:
        yazilar = yazilar.filter(
            Q(baslik__icontains =sorgu) |
            Q(icerik__icontains =sorgu)
        ).distinct()   #-> tekrar edenlerden, sadece 1 tane getir.

        #eğerki yazıların başlığı içeriyorsa, sorgudan geleni ya da
        #eğerki yazilarin içeriği, sorgudan geleni içeriyorsa bunları al.
        #Ama tekrar eden varsa , aynı veriden  2 tane gelirse, bunların sadece 1 tanesini getir.

        #yazilar tekrardan filtrelenmiş haline eşit.

    sayfa=request.GET.get('sayfa')
    paginator = Paginator(yazilar,2)


    context = {
        'yazilar':paginator.get_page(sayfa)
    }
    return render(request,"pages/anasayfa.html", context=context)






