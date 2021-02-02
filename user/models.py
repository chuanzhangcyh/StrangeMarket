from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class User(models.Model):
    open_id = models.CharField(max_length=32, unique=True)
    nickname = models.TextField(max_length=256, null=True)  # 昵称
    avatarurl = models.TextField(max_length=256, null=True)  # 头像地址，访问微信的头像地址
    gender = models.IntegerField(null=True)  # 性别，用0，1，2表示 0是未知，1是男，2是女
    country = models.TextField(max_length=256, null=True)  # 国家
    province = models.TextField(max_length=256, null=True)  # 省份
    city = models.TextField(max_length=256, null=True)  # 城市
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    last_modified = models.DateTimeField(auto_now=True)  # 最新修改时间