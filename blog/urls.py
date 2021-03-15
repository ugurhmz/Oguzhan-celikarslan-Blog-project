
from django.urls import path
from blog.views  import iletisim, anasayfa,kategori,yazilarim,detay


urlpatterns = [

    path('', anasayfa,name ='anasayfa'),
    path('iletisim', iletisim, name='iletisim'),
    path('kategori/<slug:kategoriSlug>', kategori, name='kategori'),
    #slug tipinde kategoriSlug adında. http://127.0.0.1:8000/kategori/kisisel-gelisim şeklinde.
    path('yazilarim', yazilarim, name='yazilarim'),
    path('detay/<slug:slug>', detay, name='detay'),

]