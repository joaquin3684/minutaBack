# Generated by Django 2.1.4 on 2019-01-10 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minuta', '0006_auto_20190106_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='responsabilidad',
            old_name='asistentes',
            new_name='responsables',
        ),
        migrations.AddField(
            model_name='responsabilidad',
            name='minuta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='responsabilidades', to='minuta.Minuta'),
            preserve_default=False,
        ),
    ]
