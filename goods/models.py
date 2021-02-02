from django.db import models

# Create your models here.

class Goods(models.Model):  #上传图片
    title = models.TextField()
    image_path = models.ImageField(upload_to='images')
    des = models.TextField()
    app = models.IntegerField(default=0)
    key = models.CharField(max_length=200, unique=True)
    exposure = models.IntegerField(default=1) #曝光数默认是1，以免计算点击率时出现问题
    tap = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    last_modified = models.DateTimeField(auto_now=True)  # 最新修改时间