from . import views
from django.urls import path
urlpatterns = [
    path('detail/', views.get_detail, name='get_detail'),
    path('goods/hot/', views.get_goods_by_hot, name='get_goods_by_hot'),
    path('goods/time/', views.get_goods_by_time, name='get_goods_by_time'),
    path('goods/saved/', views.get_goods_by_self_saved, name='get_goods_by_self_saved')
]