# Generated by Django 2.1.4 on 2019-01-16 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minuta', '0011_auto_20190116_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='programador',
            name='es_socio',
            field=models.BooleanField(default=True),
        ),
    ]
