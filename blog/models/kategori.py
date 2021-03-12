from django.db import models
from autoslug import AutoSlugField

class KategoriModel(models.Model):
    isim = models.CharField(max_length=30, null= True, blank= True)
    slug = AutoSlugField(populate_from='isim',unique=True)
    #Yukardaki isimden ->otomatik slug oluştur diyoruz.


    class Meta:
        db_table ='kategori'
        verbose_name_plural = 'Kategoriler'
        #Admin panelinde sol tarafta yazan Kategori modelsi düzelttik ve onun yerine
        #Kategoriler yazdık
        verbose_name = 'MyKategori'

    def __str__(self):
        return self.isim