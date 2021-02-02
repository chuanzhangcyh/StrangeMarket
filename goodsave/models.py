from django.db import models

# Create your models here.

class GoodSave(models.Model):
    open_id = models.CharField(max_length=32)
    good_id = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    last_modified = models.DateTimeField(auto_now=True)  # 最新修改时间