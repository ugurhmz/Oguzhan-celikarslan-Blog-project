
from django.urls import path
from blog.views  import iletisim, anasayfa,kategori,yazilarim,yazi_ekle,yazi_guncelle, yazi_sil,yorum_sil, DetayView
from django.views.generic  import TemplateView, RedirectView


urlpatterns = [

    path('', anasayfa,name ='anasayfa'),
    path('hakkimda',TemplateView.as_view(
        template_name='pages/hakkimda.html'
    ),name='hakkimda'),
    path('yonlendir',RedirectView.as_view(
        url='https://www.google.com'
    ), name='yonlendir'),
    path('iletisim', iletisim, name='iletisim'),
    path('kategori/<slug:kategoriSlug>', kategori, name='kategori'),
    #slug tipinde kategoriSlug adında. http://127.0.0.1:8000/kategori/kisisel-gelisim şeklinde.
    path('yazilarim', yazilarim, name='yazilarim'),
    # path('detay/<slug:slug>', detay, name='detay'),
    path('detay/<slug:slug>', DetayView.as_view(), name='detay'), #ClassBase Kullandık

    path('yazi-ekle',yazi_ekle, name='yazi-ekle'),
    path('yazi-guncelle/<slug:slug>',yazi_guncelle, name='yazi-guncelle'),
    path('yazi-sil/<slug:slug>', yazi_sil, name='yazi-sil'),
    path('yorum-sil/<int:id>',yorum_sil, name='yorum-sil'),

]