from django.contrib import admin
from django.urls import path,include
from seller import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",views.home,name="home"),
    path("index/",views.index,name="index"),
    path("crops/",views.crops,name="crops"),
    path("about/",views.about,name="about"),
    path("Request/",views.Request,name="Request"),
    path("login/",views.login,name='login'),
    path("logout/",views.logout,name='logout'),
    path("signup/",views.signup,name='signup'),
    path("sell/",views.sell,name="sell"),
    path('firut/', views.firut, name='firut'),
    path('vege/',views.Vege,name="vege"),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)