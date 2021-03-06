from django.urls import path
from .import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('products', views.products),
    path('vests', views.vests),
    path('Pants', views.Pants),
    path('Belts', views.Belts),
    path('Shoes', views.Shoes),
    path('Shirts', views.Shirts),
    path('Ties', views.Ties),
    path('View/<int:id>/', views.View),
    path('sales', views.sales),
    path('about_us', views.about_us),
    path('sign_in', views.sign_in),
    path('sign_up', views.sign_up),
    path('sign_upInterface', views.sign_upInterface),
    path('Cart', views.Cart),
    path('login', views.login),
    path('logout', views.logout),
    path('addCart/<int:id>', views.addCart),
    path('setQuality/<int:CartID>/<int:Quanlity>/', views.setQuality),
    path('checkout', views.checkout),
    path('setBill', views.setBill),
    path('yourOrder', views.yourOrder),
    path('Search/<str:Name>', views.Search),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)