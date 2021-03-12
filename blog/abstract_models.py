# Tekrar eden kodları alacağız buraya, TABLOSAL Hiç bir karşılığı olmayacak.

from django.db import models


class DateAbstractModel(models.Model):
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    duzenlenme_tarihi = models.DateTimeField(auto_now=True)  # Otomatik düzenlenme olduğunda tarih ver.



    class Meta:
        abstract = True

        """
        (1)Ortak alanları ,soyut bir modelin içerisinde  grupluyoruz.
        (2) Ortak anları aldığımıza göre  oluşturulan yerlerde sil.
        
        """