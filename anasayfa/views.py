from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from .models import AyasTarihi
from .models import GezilecekYer, KoyMahalle, Diger


# Create your views here.

def anasayfa(request):
    return render(request, 'anasayfa2.html')

def ayas_tarihi(request):
    """Ayaş Tarihi sayfası - Ayaş'ın tarihi bilgileri"""
    tarih_bilgileri = AyasTarihi.objects.order_by('-tarih', '-saat')
    return render(request, 'ayas_tarihi.html', {'etkinlikler': tarih_bilgileri})

def gezilecek_yerler(request):
    """Gezilecek Yerler sayfası"""
    yerler = GezilecekYer.objects.all().order_by('-tarih')
    return render(request, 'gezilecek_yerler.html', {'duyurular': yerler})

def guncel_haberler(request):
    """Güncel Haberler sayfası"""
    from .models import GuncelHaber
    haberler = GuncelHaber.objects.all().order_by('-tarih')
    return render(request, 'guncel_haberler.html', {'ayas_bilgiler': haberler})

def koyler_mahalleler(request):
    """Köyler ve Mahalleler sayfası"""
    koyler = KoyMahalle.objects.all().order_by('-tarih')
    return render(request, 'koyler_mahalleler.html', {'faydali_bilgiler': koyler})

def diger(request):
    """Diğer sayfası"""
    diger_items = Diger.objects.all().order_by('-tarih')
    return render(request, 'diger.html', {'diger_items': diger_items})

def galeri(request):
    return render(request, 'galeri.html')

def iletisim(request):
    return render(request, 'contact.html')

def contact(request):
    from django.core.mail import send_mail
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            subject = f'Yeni İletişim Mesajı: {name}'
            body = f'Gönderen: {name} <{email}>\n\nMesaj:\n{message}'
            send_mail(
                subject,
                body,
                'ozansari9@gmail.com',  # Change this to your sender email if needed
                ['ozansardogan379@gmail.com'],
                fail_silently=False,
            )
            success = True
    return render(request, 'contact.html', {'success': success})

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/admin/')
        else:
            error = 'Kullanıcı adı veya şifre yanlış.'
    return render(request, 'login.html', {'error': error})



