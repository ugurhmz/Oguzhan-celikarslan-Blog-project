from django.shortcuts import render,redirect,get_object_or_404
from blog.forms import YaziGuncelleFormModel
from blog.models import YazilarModel
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def yazi_guncelle(request,slug):
    yazi = get_object_or_404(YazilarModel, slug=slug, yazar=request.user)
    # Eğerki YazilarModel'inden slug'ı eşit olan, yazarıda giriş yapmış olan kullanıcı var ise
    form = YaziGuncelleFormModel(request.POST or None, files=request.FILES or None, instance =yazi)

    #sayfaya POST isteğin yapılşmış ise, request.POST isteği gelsin,yoksa none, files ile
    #sayafa gönderilmiş dosya varsa  al bunu, yoksa None, instance ilede duzenlemek istediğimiz
    #formun içinde otomatik olarak dolu gelecek

    if form.is_valid():
        form.save()
        return redirect('detay', slug=yazi.slug)
    #eğerki form güncellenmiş olanlar valid ise bu formu save yap, bunlar başarılı olduktan sonra
    #beni guncellemiş olduğum yazinin detayına at




    context = {
        'form':form,
    }

    return render(request,"pages/yazi-guncelle.html", context=context)