# Generated by Django 3.0.3 on 2020-03-13 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('body_mass_calculator', '0004_auto_20200305_1046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bodymassindex',
            options={'verbose_name': 'Индекс массы тела', 'verbose_name_plural': 'Индекс масс тел'},
        ),
        migrations.AlterModelOptions(
            name='mainpersondata',
            options={'verbose_name': 'Основные данные пользователя', 'verbose_name_plural': 'Основные данные пользователей'},
        ),
        migrations.AddField(
            model_name='mainpersondata',
            name='smoking',
            field=models.BooleanField(default=False, verbose_name='Курение'),
        ),
        migrations.AlterField(
            model_name='bodymassindex',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='bodymassindex',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Индекс массы тела'),
        ),
        migrations.AlterField(
            model_name='mainpersondata',
            name='age',
            field=models.PositiveSmallIntegerField(verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='mainpersondata',
            name='height',
            field=models.PositiveSmallIntegerField(verbose_name='Рост'),
        ),
        migrations.AlterField(
            model_name='mainpersondata',
            name='name',
            field=models.CharField(max_length=15, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='mainpersondata',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='mainpersondata',
            name='sex',
            field=models.CharField(choices=[('M', 'Муж.'), ('F', 'Жен.')], max_length=6, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='mainpersondata',
            name='weight',
            field=models.PositiveSmallIntegerField(verbose_name='Вес'),
        ),
    ]
