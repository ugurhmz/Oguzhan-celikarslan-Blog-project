from django.shortcuts import render, redirect
from blog.forms import IletisimForm



def iletisim(request):
      form = IletisimForm()

      if request.method =="POST":
          form =IletisimForm(request.POST) #buradaki veriyi alıyor, forma gönderiyor.
          if form.is_valid():
            # iletisim = IletisimModel() #Çekmek istenilen veri
            # iletisim.email = form.cleaned_data['email']
            # iletisim.isim_soyisim = form.cleaned_data['isim_soyisim']
            # iletisim.mesaj = form.cleaned_data['mesaj']
            #iletisim.save()

            form.save() #ModelForm'un sağladığı -> kendisi hallediyor.
            form.send_email(mesaj=form.cleaned_data.get('mesaj'))
            return redirect('anasayfa')


      context= {
        'form':form
      }

      return render(request,"pages/iletisim.html", context=context)
