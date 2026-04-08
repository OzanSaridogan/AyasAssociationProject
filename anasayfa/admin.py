from django.contrib import admin

from .models import AyasTarihi, GezilecekYer, KoyMahalle, GuncelHaber, ContactMessage, Diger, Poem

admin.site.register(AyasTarihi)
admin.site.register(GezilecekYer)
admin.site.register(KoyMahalle)
admin.site.register(GuncelHaber)
admin.site.register(ContactMessage)
admin.site.register(Diger)
admin.site.register(Poem)
