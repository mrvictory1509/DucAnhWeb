from django.urls import path
from .import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('products', views.products),
    path('sales', views.sales),
    path('contacts', views.contacts),
    path('about_us', views.about_us),
    path('sign_in', views.sign_in),
    path('sign_up', views.sign_up),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)