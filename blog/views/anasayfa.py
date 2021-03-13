from django.shortcuts import render
from blog.models import YazilarModel


def anasayfa(request):
    yazilar = YazilarModel.objects.all()


    context = {
        'yazilar':yazilar
    }
    return render(request,"pages/anasayfa.html", context=context)