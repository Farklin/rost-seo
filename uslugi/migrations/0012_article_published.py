# Generated by Django 3.0.4 on 2020-10-03 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uslugi', '0011_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='published',
            field=models.BooleanField(default='True', verbose_name='Публикация'),
        ),
    ]