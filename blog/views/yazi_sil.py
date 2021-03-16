from django.contrib.auth.decorators import login_required
from blog.models import YazilarModel
from django.shortcuts import  get_object_or_404

@login_required(login_url='/')
def yazi_sil(request,slug): #belli başlı sluglı olanı silecez
    pass
