from django.urls import path,include
from . import views


urlpatterns= [
    path('', views.mainheart, name='mainheart'),
    path('/result2',views.formInfo2, name='result2'),
]