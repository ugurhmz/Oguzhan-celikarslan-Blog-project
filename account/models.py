
# AMACIMIZ ->DJANGONUN auth_user classına ekleme yapmak: User avatar istiyoruz.

from django.db import models
from django.contrib.auth.models import AbstractUser
#AbstractUser -> Bunu miras alıyoruz, içindekileri bir daha yazmamak için


class CustomUserModel(AbstractUser): #AbbtractUser içindeki her şeye sahibim şimdi.
    avatar = models.ImageField(upload_to='avatar/', null=True, blank = True)
            # O halde 1 tanede avatar ekleyelim buraya.

    class Meta:
        db_table = 'user_avatar'
        verbose_name = 'KullanıcıResim'
        verbose_name_plural = 'KullanıcılarResim'


    def __str__(self):
        return self.username

    """
    NOT ->ŞİMDİK DEMEMİZ GEREK :
    (1)Django senin kullandığın default User modelini, biz kullanmak istemiyoruz.
    Bunun yerine Kendi hazırlamış olduğumuz(+ avatar) 'lı olanı kullanmak istiyoruz.
    
    (2)  Root(config) -> settings.py en alta git
    
    (3)  AUTH_USER_MODEL = 'account.CustomUserModel'          # Aynen böyle eklke
    
    (4)  python manage.py makemigrations yap -> Uyarı aldıktan sonra
    
    (5)  yazi.py & yorum.py içindeki ForeignKey(User) burdaki Useri şunla değiştir
    
    (6)  yazar = models.ForeignKey('account.CustomUserModel', ........ )
         yazan = models.ForeignKey('account.CustomUserModel', ..........)
         
     (7) python manage.py makemigrations
     
     (8)  python manage.py migrate         
        Hata vericek:
        
        Çözümü : db_sqlite3 sil.
        
        TEKRARR ->  python manage.py migrate yap 
        
        python manage.py createsuperuser      oluştur...
        
        işlemler bu kadar.... 
    """