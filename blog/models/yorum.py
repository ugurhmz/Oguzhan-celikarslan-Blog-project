from django.db import models
from blog.models import YazilarModel
from blog.abstract_models import  DateAbstractModel


class YorumModel(DateAbstractModel):
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



    class Meta:
        db_table ='yorum'
        verbose_name_plural = "Tüm Yorumlar"
        verbose_name = 'Yorum'

    def __str__(self):
        return self.yazan.username #yazan ForeignKey olduğu için -> yazan.username dedik.