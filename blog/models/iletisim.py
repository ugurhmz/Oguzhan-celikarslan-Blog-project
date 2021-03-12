from django.db import models



class IletisimModel(models.Model):
    email = models.EmailField(max_length=200) #Email valid olması için -> EmailField yaptık.
    isim_soyisim = models.CharField(max_length = 200)
    mesaj = models.TextField()
    gonderim_tarihi = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table='iletisim'
        verbose_name_plural = 'İletişim'
        verbose_name = 'İletişim'


    def __str__(self):
        return self.email