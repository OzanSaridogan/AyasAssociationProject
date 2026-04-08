# Generated migration for Poem model

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0007_diger_pdf_dosya'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=200, verbose_name='Başlık')),
                ('yazar', models.CharField(blank=True, max_length=200, verbose_name='Yazar')),
                ('icerik', models.TextField(verbose_name='Şiir İçeriği')),
                ('resim', models.ImageField(blank=True, null=True, upload_to='poems/', verbose_name='Görsel')),
                ('tarih', models.DateField(auto_now_add=True, verbose_name='Tarih')),
            ],
            options={
                'verbose_name': 'Şiir',
                'verbose_name_plural': 'Şiirler',
            },
        ),
    ]
