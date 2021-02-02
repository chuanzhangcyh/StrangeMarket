from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http.response import HttpResponse
import json
import requests
from .models import User
import hashlib
# Create your views here.
def login_by_wxcode(request):
    openid = request.session.get('openid')
    if openid: #如果是登陆态 直接返回登陆完成
        print('okk')
        return HttpResponse('login ok')

    else:
        code = request.GET.get('code')  # 通过GET拿到GET方式上传的微信id
        appid = 'wxfd73795bc1ab347e'
        appsecret = 'd765336aa223115560397775309e7eaa'
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code' % \
              (appid, appsecret, code)
        url_response = requests.get(url=url)
        data = json.loads(url_response.text)
        openid = data.get('openid')
        #session_key = data.get('session_key')
        request.session['openid'] = openid  # 保存openid到中间件
        print(request.session['openid'])
        print('ok')
        if not User.objects.filter(open_id=openid):  # 如果该用户不存在
            new_user = User(open_id=openid)
            new_user.save()
        #request.session['session_key'] = session_key  # 保存微信session_key到中间件
        #sha = hashlib.sha1()  # 通过hashlib自定义由openid和session_key相关的值
        #sha.update(openid.encode())
        #sha.update(session_key.encode())
        #digest = sha.hexdigest()  # 获得digest
        #request.session['skey'] = digest
        #data = {
            #'skey': digest}
        #data = json.dumps(data)
        return HttpResponse('login ok')



