from django.contrib import admin
from blog.models import KategoriModel,YazilarModel,YorumModel, IletisimModel



#__________________________________ YazilarAdmin ______________________________
class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('baslik','icerik','olusturulma_tarihi')
    # Yazilarimin ->baslik, icerik ve olus.tarih için arama kutusu
    list_display = ('baslik','olusturulma_tarihi','duzenlenme_tarihi') #admin panelinde görünmesini istediklerim
    list_display_links= ('baslik','olusturulma_tarihi') # Görünenlere tıklayarak ulaşma


admin.site.register(YazilarModel,YazilarAdmin)

#__________________________________ YorumlarAdmin______________________________
class YorumlarAdmin(admin.ModelAdmin):
    search_fields = ('yazan__username',)  # ForeignKey ile ilişkili olduğundan 'yazan__username' şeklindeyaptık.
    list_display = ('yazan','yazi','olusturulma_tarihi','duzenlenme_tarihi')
    list_display_links = ('yazi','olusturulma_tarihi')

admin.site.register(YorumModel, YorumlarAdmin)


##__________________________________ IletisimAdmin______________________________
@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):
    list_display = ('email','isim_soyisim','gonderim_tarihi')
    search_fields =('email','isim_soyisim')


@admin.register(KategoriModel)
class KategoriAdmin(admin.ModelAdmin):
    search_fields = ('baslik',)
