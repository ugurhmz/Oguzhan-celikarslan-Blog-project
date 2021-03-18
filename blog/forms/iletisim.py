from django import forms
from blog.models import IletisimModel
from django.core.mail import send_mail


class IletisimForm(forms.ModelForm):
    class Meta:
        model = IletisimModel
        fields =('isim_soyisim','email','mesaj') #hangi fieldları formun içinde göstermek istiyorsam
        #IletisimModel -> içinde olanları


    def send_email(self, mesaj):
        send_mail(
            subject='İletişim Formundan email var!',
            message=mesaj,
            from_email=None,
            recipient_list=['ugur.hmz52@gmail.com'],
            fail_silently=False
        )