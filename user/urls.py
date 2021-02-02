from . import views
from django.urls import path
urlpatterns = [
    path('login/', views.login_by_wxcode, name='get_wx_code'),
]