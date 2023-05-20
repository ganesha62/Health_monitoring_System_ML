from django.urls import path
from . import views

urlpatterns= [
    path('', views.mainlung, name='mainlung'),
    path('/result3',views.formInfo3, name='result3'),
]