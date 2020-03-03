# Generated by Django 3.0.3 on 2020-03-03 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('body_mass_calculator', '0002_auto_20200301_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpersondata',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
