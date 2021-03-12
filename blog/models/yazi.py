from django.db import models
from autoslug import AutoSlugField
from blog.models import  KategoriModel # ManyToManyField için ekledik
from ckeditor.fields import RichTextField
from blog.abstract_models import DateAbstractModel



class YazilarModel(DateAbstractModel):
    resim=models.ImageField(upload_to='yazi_resimleri') # resimleri yazi_resimleri alanına at.
    baslik = models.CharField(max_length = 250)
    icerik = RichTextField()

    slug = AutoSlugField(populate_from='baslik', unique=True)# Nereden oluşturcak slug-> 'baslik' tan olustursun

    kategoriler = models.ManyToManyField(KategoriModel, related_name='yazi')
    """
    (1)1 yazi ->1den fazla kategori ile ilişkilendirilebilir.ManyToManyField(TABLONUN satırları arası etkileşim)
    (2) bir kategoriye ait bütün yazilara erişmek için -> related_name='yazi'  . 
    (3) Kategoriler üzerinden Tüm ona ait yazılar
    """
    yazar = models.ForeignKey('account.CustomUserModel', on_delete = models.CASCADE,related_name='yazilar')

    """ (1) User tablosuna bağlayacaz çünkü ->
     (2) Yazar Üzerinden yazarın bütün yazılarına erişmek için yapıyoruz -> related_name=''
    (3) ForeignKey ->  Bir tabloyu, Bir başka tablo ile ilişkilendirmeye yarar.(TABLOLAR ARASI ETKİLEŞİM)
    (4) on_delete = models.CASCADE -> DataBase'den User silinirse, Ona AİT bütün yazılar silinmesi için.
    """
    class Meta:
        db_table = 'Yazilarim'
        verbose_name_plural='Yazilarim' #Admin  panel -> Lef side için gözükmesini istediğim .
        verbose_name='MyYazi'
    def __str__(self):
        return self.baslik


