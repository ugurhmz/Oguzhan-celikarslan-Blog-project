from django.contrib import admin
from blog.models import KategoriModel,YazilarModel


admin.site.register(KategoriModel)

#Admin Panelini özelleştirme
class YazilarAdmin(admin.ModelAdmin):
    search_fields = ['baslik','icerik','olusturulma_tarihi'] # Yazilarimin ->baslik, icerik ve olus.tarih için arama kutusu
    list_display = ['baslik','olusturulma_tarihi','duzenlenme_tarihi'] #admin panelinde görünmesini istediklerim
    list_display_links= ['baslik','olusturulma_tarihi'] # Görünenlere tıklayarak ulaşma



admin.site.register(YazilarModel,YazilarAdmin)
