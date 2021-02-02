from django.shortcuts import render
from django.http.response import HttpResponse
from.models import GoodSave
# Create your views here.

def save_add(request):
    open_id = request.session.get('openid')
    if not open_id:
        return HttpResponse('fail')
    else:
        good_id = request.GET.get('good_id')
        if not GoodSave.objects.filter(good_id=good_id,open_id=open_id):
            new_good_save = GoodSave(open_id=open_id,
                                     good_id=good_id
                                     )
            new_good_save.save()
            return HttpResponse('ok')
        else:
            return HttpResponse('saved')
def save_delete(request):
    open_id = request.session.get('openid')
    if not open_id:
        return HttpResponse('fail')
    else:
        good_id = request.GET.get('good_id')
        if GoodSave.objects.filter(good_id=good_id, open_id=open_id):
            GoodSave.objects.filter(good_id=good_id, open_id=open_id).delete()
            return HttpResponse('ok')
        else:
            return HttpResponse('deleted')