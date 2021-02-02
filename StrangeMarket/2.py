import time
import hashlib
import json
import requests
from utils.pdd import get_search_id
type = 'pdd.ddk.goods.promotion.url.generate'
client_id = '90a990bc143d4737b3af08b5d671fc65'
client_secret = '4dc520a203ce8f8f9d2af0205f4a12dbcf3a45cd'
timestamp = str(int(time.time())) #unix格式 单位是秒
p_id = '10326915_188461783'
goods_sign = 'c9v2ok31If1OVVbRwvfYr_1eOhYn_JKc6RMEB7'
#goods_sign = [goods_sign]
#goods_sign_list = str(goods_sign)
generate_we_app = True
search_id = get_search_id(goods_sign)
goods_sign_list = str([goods_sign])
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
print(data)
data = json.dumps(data)
res = requests.post(url=url, data=data)
res = json.loads(res.text)
print(res)
print(sign)

from utils.pdd import get_search_id,get_good_info
good_sign = 'c9v2ok31If1OVVbRwvfYr_1eOhYn_JKc6RMEB7'
search_id = get_search_id(good_sign)
res = get_good_info(good_sign, search_id)
