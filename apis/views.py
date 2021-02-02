from django.shortcuts import render

# Create your views here.
from utils.pdd import get_search_id,get_good_info
import random
import json
from goods.models import Goods
from goodsave.models import GoodSave
from django.forms import model_to_dict
from django.core import serializers
from django.http.response import HttpResponse
def get_detail(request): #获取跳转信息
    app = request.GET.get('app')
    key = request.GET.get('key')
    try: #统计点击数
        good = Goods.objects.get(key=key)
        good.tap += 1
        good.save()
    except:
        pass
    search_id = get_search_id(key)
    res = get_good_info(key, search_id)
    res = json.dumps(res)
    return HttpResponse(res, content_type='application/json')
def get_goods_by_time(request): #已最新为排序
    open_id = request.session.get('openid')
    if not open_id:
        return HttpResponse('fail')
    else:
        data = Goods.objects.all().order_by('-id') #以id排序
        saved_goods = GoodSave.objects.filter(open_id=open_id).values('good_id') #取得收藏的商品
        saved_goods_list = []
        if saved_goods:#存入列表
            for k in saved_goods:
                saved_goods_list.append(k['good_id'])
        goods = []
        for i in data:
            i = model_to_dict(i)
            i['image_path'] = 'http://127.0.0.1:8000/wrt/media/'+str(i['image_path']) #把ImageFile格式转化成str并拼接访问地址
            i['is_saved'] = 1 if i['id'] in saved_goods_list else 0 #如果id在被收藏的表里 设置属性为1
            goods.append(i)#返回一个列表
        goods = json.dumps(goods, ensure_ascii=False)#转成json

        return HttpResponse(goods, content_type='application/json')
def get_goods_by_hot(request): #推荐排序商品 点击率为主 新品为12个2+n
    open_id = request.session.get('openid')
    if not open_id:
        return HttpResponse('fail')
    else:
        saved_goods = GoodSave.objects.filter(open_id=open_id).values('good_id')  # 取得收藏的商品
        saved_goods_list = []
        if saved_goods:  # 存入列表
            for k in saved_goods:
                saved_goods_list.append(k['good_id'])

        all_data = Goods.objects.all()
        ctr_data = all_data.extra(select={'ctr' : 'tap/exposure'}).order_by('-ctr') #重要 计算点击率 并按点击率排序
        new_data = all_data.order_by('-id')[:12] #最新的12个商品
        goods = []
        try:
            for i in ctr_data:
                if i in new_data: #判断是否是新商品 如果是新商品 先不计算在总数据中，在后面再加入
                    pass
                else:
                    i = model_to_dict(i)
                    i['image_path'] = 'http://127.0.0.1:8000/wrt/media/' + str(i['image_path'])  # 把ImageFile格式转化成str并拼接访问地址
                    i['is_saved'] = 1 if i['id'] in saved_goods_list else 0  # 如果id在被收藏的表里 设置属性为1
                    goods.append(i)  # 返回一个列表
        except:
            pass
        else:
            pass

        try: #随机打乱新商品 然后插入
            new_goods = []
            new_data_list = list(range(len(new_data)))
            random.shuffle(new_data_list)
            for k in new_data_list: #先获得长度，再生成range，再变成list，再打乱顺序
                new_good = model_to_dict(new_data[k])
                new_good['image_path'] = 'http://127.0.0.1:8000/wrt/media/' + str(new_good['image_path'])# 把ImageFile格式转化成str并拼接访问地址
                new_good['is_saved'] = 1 if new_good['id'] in saved_goods_list else 0  # 如果id在被收藏的表里 设置属性为1
                new_goods.append(new_good)
            for x in range(len(new_goods)):#插入新商品
                goods.insert(1+2*x, new_goods[x])
        except:
            pass
        goods = json.dumps(goods, ensure_ascii=False)  # 转成json
        return HttpResponse(goods, content_type='application/json')

def get_goods_by_self_saved(request):
    open_id = request.session.get('openid')
    if not open_id:
        return HttpResponse('fail')
    else:
        goods = []
        saved_goods = GoodSave.objects.filter(open_id=open_id).order_by('-id')
        if saved_goods:
            for i in saved_goods:
                i = model_to_dict(i)
                id = i['good_id']
                good = Goods.objects.get(id=id)
                good = model_to_dict(good)
                good['image_path'] = 'http://127.0.0.1:8000/wrt/media/' + str(good['image_path'])
                good['is_saved'] = 1
                goods.append(good)
            goods = json.dumps(goods, ensure_ascii=False)
            return HttpResponse(goods, content_type='application/json')
        else:
            return HttpResponse('no saved')