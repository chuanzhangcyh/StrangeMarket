from django.contrib import admin

# Register your models here.
from .models import Goods
admin.site.register(Goods)  #使管理后台支持上传图片