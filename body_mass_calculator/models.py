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

    MALE = 'M'
    FEMALE = 'F'
    SEX_TYPES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    person = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    sex = models.CharField(max_length=6, choices=SEX_TYPES)
    age = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()


class BodyMassIndex(models.Model):
    class Meta:
        db_table = 'body_mass_index'
        constraints = (
            models.CheckConstraint(check=models.Q(value__gte=0), name='value_gte_0'),
        )

    value = models.DecimalField(max_digits=5, decimal_places=2)
    person = models.ForeignKey(User, on_delete=models.CASCADE)


@receiver(post_save, sender=MainPersonData, dispatch_uid='calculate_body_mass_index_value')
def calculate_body_mass_index(sender, instance, **kwargs) -> None:
    user = instance.person
    value = instance.weight / pow((instance.height / 100), 2)
    body_mass_index = BodyMassIndex(value=value, person=user)
    body_mass_index.save()
