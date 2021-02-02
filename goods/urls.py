from . import views
from django.urls import path
urlpatterns = [
    path('exposure/', views.get_exposure, name='get_exposure'),

]