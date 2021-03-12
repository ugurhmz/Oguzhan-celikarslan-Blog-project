from django.contrib import admin
from blog.models import KategoriModel,YazilarModel,YorumModel


admin.site.register(KategoriModel)

#Admin Panelini özelleştirme
class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('baslik','icerik','olusturulma_tarihi')
    # Yazilarimin ->baslik, icerik ve olus.tarih için arama kutusu
    list_display = ('baslik','olusturulma_tarihi','duzenlenme_tarihi') #admin panelinde görünmesini istediklerim
    list_display_links= ('baslik','olusturulma_tarihi') # Görünenlere tıklayarak ulaşma


admin.site.register(YazilarModel,YazilarAdmin)


class YorumlarAdmin(admin.ModelAdmin):
    search_fields = ('yazan__username',)  # ForeignKey ile ilişkili olduğundan 'yazan__username' şeklindeyaptık.
    list_display = ('yazan','yazi','olusturulma_tarihi','guncellenme_tarihi')
    list_display_links = ('yazi','olusturulma_tarihi')

admin.site.register(YorumModel, YorumlarAdmin)