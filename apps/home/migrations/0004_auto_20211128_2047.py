# Generated by Django 3.2.5 on 2021-11-28 17:47

import apps.home.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_profildetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profildetay',
            name='HESCode',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True, validators=[apps.home.models.validateHesCode]),
        ),
        migrations.AlterField(
            model_name='profildetay',
            name='TC',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True, validators=[apps.home.models.validateEven]),
        ),
        migrations.AlterField(
            model_name='profildetay',
            name='adress',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profildetay',
            name='birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='Doğum Tarihiniz'),
        ),
        migrations.AlterField(
            model_name='profildetay',
            name='gender',
            field=models.CharField(blank=True, choices=[('KIZ', 'Kız'), ('erkek', 'Erkek'), ('diger', 'Diğer')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='profildetay',
            name='isWorking',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='profildetay',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.jobstable'),
        ),
    ]
