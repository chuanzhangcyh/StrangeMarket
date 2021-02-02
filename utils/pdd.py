import time
import hashlib
import json
import requests
client_id = '90a990bc143d4737b3af08b5d671fc65'
client_secret = '4dc520a203ce8f8f9d2af0205f4a12dbcf3a45cd'

def get_search_id(good_sign): #获取pdd的search_id 拼多多后台表示可以增加收益，具体如何不清楚
    client_id = '90a990bc143d4737b3af08b5d671fc65'
    client_secret = '4dc520a203ce8f8f9d2af0205f4a12dbcf3a45cd'
    good_sign = [good_sign]
    goods_sign_list = str(good_sign)
    type = 'pdd.ddk.goods.search'
    timestamp = str(int(time.time()))
    base_sign = client_secret + 'client_id' + client_id + 'goods_sign_list' + goods_sign_list + 'timestamp' + timestamp + 'type' + type + client_secret
    sign = hashlib.md5()
    sign.update(base_sign.encode(encoding='utf-8'))
    sign = sign.hexdigest()
    sign = sign.upper()
    url = 'https://gw-api.pinduoduo.com/api/router'
    header = 'content-type: application/json'
    data = {}
    data['type'] = type
    data['client_id'] = client_id
    data['timestamp'] = timestamp
    data['sign'] = sign
    data['goods_sign_list'] = goods_sign_list
    data = json.dumps(data)
    res = requests.post(url=url, data=data)

    res = json.loads(res.text)
    search_id = res['goods_search_response']['search_id']
    return search_id
def get_good_info(good_sign, search_id):
    search_id = search_id
    goods_sign_list = str([good_sign])
    p_id = '10326915_188461783'
    type = 'pdd.ddk.goods.promotion.url.generate'
    timestamp = str(int(time.time()))
    generate_we_app = True
    a = client_secret + 'client_id' + client_id + 'generate_we_app' + 'true' + 'goods_sign_list' + goods_sign_list + 'p_id' + p_id + 'search_id' + search_id +'timestamp' + timestamp + 'type' + type + client_secret
    sign = hashlib.md5()
    sign.update(a.encode(encoding='utf-8'))
    sign = sign.hexdigest()
    sign = sign.upper()
    url = 'https://gw-api.pinduoduo.com/api/router'
    header = 'content-type: application/json'
    data = {}
    data['type'] = type
    data['client_id'] = client_id
    data['timestamp'] = timestamp
    data['sign'] = sign
    data['p_id'] = p_id
    data['search_id'] = search_id
    data['goods_sign_list'] = goods_sign_list
    data['generate_we_app'] = generate_we_app
    data = json.dumps(data)
    res = requests.post(url=url, data=data)
    res = json.loads(res.text)
    res = res['goods_promotion_url_generate_response']['goods_promotion_url_list'][0]['we_app_info']
    return res