from django import template
from blog.models import KategoriModel

register = template.Library()  #template taglarını ve filterlerini kayıt etmek için kullanılır.



@register.simple_tag
def kategori_list():
    kategoriler = KategoriModel.objects.all()
    return kategoriler
