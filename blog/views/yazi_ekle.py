from django.shortcuts import render,redirect
from blog.forms import YaziEkleModelForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def yazi_ekle(request):
    form = YaziEkleModelForm(request.POST or None, files=request.FILES or None)
    #otomatik olarak post ile gelen verileri formun içine eklemek

    if form.is_valid():
        yazi = form.save(commit=False)
        yazi.yazar = request.user
        yazi.save()
        form.save_m2m()
        return redirect("detay", slug=yazi.slug)

    context = {
        'form':form,
    }

    return render(request,"pages/yazi-ekle.html", context=context)