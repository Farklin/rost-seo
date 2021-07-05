# Generated by Django 3.0.4 on 2020-09-13 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uslugi', '0004_auto_20200829_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='uslugi.Category', verbose_name='Родительская категория'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank='null', null=True, upload_to='images/', verbose_name='Изображение'),
        ),
    ]
