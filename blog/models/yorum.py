from django.db import models
from django.contrib.auth.models import User
from blog.models import YazilarModel

class YorumModel(models.Model):
    yazan = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='yorum')
    """
    (1) yazanı -> User ile eşleştiriyoruz. User üzerinden de bu kullanıcının yorumlarına erişebiliyoruz.
    (2) Her yorumun->Bir yazanı olduğundan User ile ilişkilendirmek gerek.-> ForeignKey
    (3) Yazan kişinin yorumlarına erişmek için -> related_name = 'yorum' """

    yazi = models.ForeignKey(YazilarModel, on_delete = models.CASCADE,related_name='yorumlar')
    """ 
    (1) Her yorum bir yazıya yazıldığı için, yazı ile ilişkilendircez ->ForeignKey
    (2) on_delete ile  yazi silinirse eğer, ona yapılan yorumlarıda sil demiş olduk.
    (3) yazinin yorumlarına erişmek için -> related_name='yorumlar'    """

    yorum = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    guncellenme_tarihi=models.DateTimeField(auto_now=True)


    class Meta:
        db_table ='yorum'
        verbose_name_plural = "Tüm Yorumlar"
        verbose_name = 'Yorum'

    def __str__(self):
        return self.yazan.username #yazan ForeignKey olduğu için -> yazan.username dedik.