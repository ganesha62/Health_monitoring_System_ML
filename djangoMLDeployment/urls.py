from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
   # path('', include('chronicapp.urls')),
    #path('', include('irisApp.urls')),
    path('admin/', admin.site.urls),
    path('', views.mainpage),
    path('mainpage', views.mainpage),
    path('kidney',include('irisApp.urls')),
    path('heart',include('heartApp.urls')),
    path('lung',include('lungApp.urls')),
]
