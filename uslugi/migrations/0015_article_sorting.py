# Generated by Django 3.0.4 on 2020-11-04 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uslugi', '0014_applicationform'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='sorting',
            field=models.IntegerField(default='1', max_length=1, null=True, verbose_name='Сортировка'),
        ),
    ]