from math import pow

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class MainPersonData(models.Model):
    class Meta:
        db_table = 'main_data'
        constraints = (
            models.CheckConstraint(check=models.Q(age__gte=18), name='age_gte_18'),
        )
        verbose_name = 'Основные данные пользователя'
        verbose_name_plural = 'Основные данные пользователей'

    MALE = 'M'
    FEMALE = 'F'
    SEX_TYPES = (
        (MALE, 'Муж.'),
        (FEMALE, 'Жен.'),
    )

    person = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, verbose_name='Пользователь')
    name = models.CharField(max_length=15, verbose_name='Имя')
    sex = models.CharField(max_length=6, choices=SEX_TYPES, verbose_name='Пол')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')
    height = models.PositiveSmallIntegerField(verbose_name='Рост')
    weight = models.PositiveSmallIntegerField(verbose_name='Вес')
    smoking = models.BooleanField(verbose_name='Курение', default=False)

    def __str__(self):
        return self.person.username


class BodyMassIndex(models.Model):
    class Meta:
        db_table = 'body_mass_index'
        constraints = (
            models.CheckConstraint(check=models.Q(value__gte=0), name='value_gte_0'),
        )

        verbose_name = 'Индекс массы тела'
        verbose_name_plural = 'Индекс масс тел'

    value = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Индекс массы тела')
    person = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.person.name


@receiver(post_save, sender=MainPersonData, dispatch_uid='calculate_body_mass_index_value')
def calculate_body_mass_index(sender, instance, **kwargs) -> None:
    user = instance.person
    value = instance.weight / pow((instance.height / 100), 2)
    previous_data = BodyMassIndex.objects.filter(person=user)
    if previous_data.exists():
        previous_data.update(value=value)
    else:
        body_mass_index = BodyMassIndex(value=value, person=user)
        body_mass_index.save()
