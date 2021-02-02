import top.api
req = top.api.TbkTpwdCreateRequest(domain='gw.api.taobao.com', port=80)
appkey = 32446409
secret = 'aa82a95c1c8c45f10ee21790303f89c3'
req.set_app_info(top.appinfo(appkey, secret))
req.url = 'https://s.click.taobao.com/kcOCgru'
req.text = '复制复制复制'
reps = req.getResponse()
print(reps)


