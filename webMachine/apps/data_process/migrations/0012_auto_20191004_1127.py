# Generated by Django 2.2.5 on 2019-10-04 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_process', '0011_auto_20191004_1125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='firstcatage',
            options={'ordering': ['first_catage_order'], 'verbose_name': '一级目录', 'verbose_name_plural': '一级目录'},
        ),
        migrations.AlterField(
            model_name='firstcatage',
            name='first_catage_slug',
            field=models.SlugField(help_text='一级目录连接,禁止为空', unique=True, verbose_name='一级目录连接'),
        ),
        migrations.AlterField(
            model_name='secondcatage',
            name='second_catage_slug',
            field=models.SlugField(help_text='二级目录连接,禁止为空', unique=True, verbose_name='二级目录连接'),
        ),
    ]