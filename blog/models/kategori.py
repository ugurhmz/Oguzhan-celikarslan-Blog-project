from django.db import models
from autoslug import AutoSlugField

class KategoriModel(models.Model):
    isim = models.CharField(max_length=30, null= True, blank= True)
    slug = AutoSlugField(populate_from='isim',unique=True) #Yukardaki isimden ->otomatik slug oluştur diyoruz.


    class Meta:
        db_table ='kategori'