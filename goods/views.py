import json
from .models import Goods
from django.http.response import HttpResponse
def get_exposure(request): #实时更新曝光
    post_data = request.body.decode('utf-8')
    post_data = json.loads(post_data)
    data = post_data['exposure_data']
    set_data = set(data)
    res = {}
    for i in set_data:
        res[i] = data.count(i)
    goods_list = list(set_data)
    goods = Goods.objects.filter(id__in=goods_list)
    for k in set_data:
        try:
            good = goods.get(id=k)
            good.exposure += res[k]
            good.save()
        except:
            pass
        else:
            pass
    return HttpResponse('ok')
