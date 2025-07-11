from django.urls import path
from byer import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("buyreindex/", views.buyreindex, name="buyreindex"),
    path("buyreabout/",views.buyreabout,name="buyreabout"),
    path("buyrecontact/",views.buyrecontact,name="buyrecontact"),
    path("buyerlogin/",views.buyerlogin,name="buyerlogin"),
    path("buyersginup/",views.buyersginup,name="buyersginup"),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('buyerlogout/', views.buyer_logout, name='buyerlogout'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
