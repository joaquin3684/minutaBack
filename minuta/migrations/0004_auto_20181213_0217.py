# Generated by Django 2.1.4 on 2018-12-13 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minuta', '0003_auto_20181209_0341'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistente',
            name='mail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='definicion',
            name='texto',
            field=models.TextField(default="1"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='minuta',
            name='descripcion',
            field=models.TextField(default="1"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='minuta',
            name='fecha',
            field=models.DateField(blank=True, null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='responsabilidad',
            name='tarea',
            field=models.TextField(default="1"),
            preserve_default=False,
        ),
    ]
