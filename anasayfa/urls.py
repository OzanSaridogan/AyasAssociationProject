from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('anasayfa/', views.anasayfa, name='anasayfa'),
    path('ayas-tarihi/', views.ayas_tarihi, name='ayas_tarihi'),
    path('gezilecek-yerler/', views.gezilecek_yerler, name='gezilecek_yerler'),
    path('guncel-haberler/', views.guncel_haberler, name='guncel_haberler'),
    path('koyler-mahalleler/', views.koyler_mahalleler, name='koyler_mahalleler'),
    path('galeri/', views.galeri, name='galeri'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('contact/', views.contact, name='contact'),  # Yeni iletişim sayfası için
    path('Login/', views.login_view, name='login'),  # Giriş sayfası
]

urlpatterns += staticfiles_urlpatterns()  # Static files için URL kalıplarını ekle
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Media files için URL
