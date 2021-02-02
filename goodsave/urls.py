from . import views
from django.urls import path
urlpatterns = [
    path('save/', views.save_add, name='save_add'),
    path('delete/', views.save_delete, name='save_delete'),
]