# Generated by Django 3.2.9 on 2021-11-22 12:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0005_alter_buyerdata_abrv'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotationdata',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
