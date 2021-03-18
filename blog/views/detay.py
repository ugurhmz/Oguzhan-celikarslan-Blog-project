from django.shortcuts import render,get_object_or_404,redirect
from blog.models import YazilarModel
from blog.forms import YorumEkleModelForm
from django.views import View
from django.contrib import messages

import logging

logger = logging.getLogger('konu_okuma')

class DetayView(View): #View -> Çeşitli Http metodlarına karşın cevap üretir.
        http_method_names=['get','post']
        yorum_ekleme_formu = YorumEkleModelForm


        def get(self,request,slug):
            yazi = get_object_or_404(YazilarModel, slug=slug)
            if request.user.is_authenticated:
                logger.info('konu okundu : '+request.user.username)

            yorumlar =yazi.yorumlar.all()

            context = {
                'yazi': yazi,
                'yorumlar': yorumlar,
                'yorum_ekleme_formu':self.yorum_ekleme_formu
            }



            return render(request,"pages/detay.html",context=context )



        def post(self,request,slug):
            yazi = get_object_or_404(YazilarModel, slug=slug)
            yorum_ekle_form = self.yorum_ekleme_formu(data=request.POST)
            if yorum_ekle_form.is_valid():
                yorum = yorum_ekle_form.save(commit=False)
                yorum.yazan = request.user
                yorum.yazi = yazi
                yorum.save()
                messages.success(request,"Yorum eklendi")

            return redirect('detay',slug=slug)



#
#
# #DetayView kullandık
# def detay(request, slug):
#     yazi = get_object_or_404(YazilarModel, slug=slug)
#     yorumlar = yazi.yorumlar.all()
#
#     if request.method=='POST':
#         yorum_ekle_form = YorumEkleModelForm(data=request.POST)
#         if yorum_ekle_form.is_valid():
#             yorum=yorum_ekle_form.save(commit=False)
#             yorum.yazan =  request.user
#             yorum.yazi = yazi
#             yorum.save()
#
#
#     yorum_ekle_form = YorumEkleModelForm()
#
#
#     context = {
#         'yazi':yazi,
#         'yorumlar':yorumlar,
#         'yorum_ekle_form':yorum_ekle_form,
#     }
#
#     return render(request,"pages/detay.html", context = context)