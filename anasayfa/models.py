
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField("Ad Soyad", max_length=100)
    email = models.EmailField("E-posta")
    message = models.TextField("Mesaj")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class GuncelHaber(models.Model):
    """Güncel Haberler - Dernek faaliyetleri ve güncel gelişmeler"""
    baslik = models.CharField("Başlık", max_length=200)
    aciklama = models.TextField("Açıklama")
    resim = models.ImageField("Görsel", upload_to='guncel_haberler/', blank=True, null=True)
    tarih = models.DateField("Tarih", auto_now_add=True)

    class Meta:
        verbose_name = "Güncel Haber"
        verbose_name_plural = "Güncel Haberler"

    def __str__(self):
        return self.baslik


class AyasTarihi(models.Model):
    """Ayaş Tarihi - Ayaş'ın tarihi bilgileri"""
    baslik = models.CharField("Başlık", max_length=200)
    aciklama = models.TextField("Açıklama")
    tarih = models.DateField("Tarih")
    saat = models.TimeField("Saat")
    yer = models.CharField("Yer", max_length=200)
    resim = models.ImageField("Görsel", upload_to='ayas_tarihi/', blank=True, null=True)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ayaş Tarihi"
        verbose_name_plural = "Ayaş Tarihi"

    def __str__(self):
        return self.baslik

class GezilecekYer(models.Model):
    """Gezilecek Yerler - Ayaş'ta keşfedilecek güzellikler"""
    baslik = models.CharField("Başlık", max_length=200)
    aciklama = models.TextField("Açıklama")
    tarih = models.DateField("Tarih", auto_now_add=True)
    resim = models.ImageField("Görsel", upload_to='gezilecek_yerler/', blank=True, null=True)

    class Meta:
        verbose_name = "Gezilecek Yer"
        verbose_name_plural = "Gezilecek Yerler"

    def __str__(self):
        return self.baslik

class KoyMahalle(models.Model):
    """Köyler ve Mahalleler - Ayaş'ın köyleri ve mahalleleri"""
    baslik = models.CharField("Başlık", max_length=200)
    aciklama = models.TextField("Açıklama")
    resim = models.ImageField("Görsel", upload_to='koyler_mahalleler/', blank=True, null=True)
    tarih = models.DateField("Tarih", auto_now_add=True)

    class Meta:
        verbose_name = "Köy/Mahalle"
        verbose_name_plural = "Köyler ve Mahalleler"

    def __str__(self):
        return self.baslik

class Diger(models.Model):
    """Diğer - Diğer içerikler ve bilgiler"""
    baslik = models.CharField("Başlık", max_length=200)
    aciklama = models.TextField("Açıklama")
    resim = models.ImageField("Görsel", upload_to='diger/', blank=True, null=True)
    tarih = models.DateField("Tarih", auto_now_add=True)

    class Meta:
        verbose_name = "Diğer"
        verbose_name_plural = "Diğer"

    def __str__(self):
        return self.baslik
