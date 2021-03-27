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
    path('Cart', views.Cart),
    path('add_Cart/<int:id>/', views.add_Cart),
    path('login', views.login),
    path('logout', views.logout),
    path('addCart/<int:id>', views.addCart),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)