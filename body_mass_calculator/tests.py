from decimal import Decimal

from django.test import TestCase, TransactionTestCase
from django.db.utils import IntegrityError

from .models import MainPersonData, BodyMassIndex, User

TEST_USER_NAME = 'test_user'
TEST_EMAIL = 'test@mail.ru'
TEST_PASSWORD = 'test_password'
TEST_AGE = 22
TEST_HEIGHT = 180
TEST_WEIGHT = 180
TEST_SEX = MainPersonData.MALE
TEST_RESULT = Decimal('55.56')
TEST_WRONG_AGE = 13
TEST_UPDATE_HEIGHT = 100
TEST_UPDATE_WEIGHT = 40
TEST_UPDATE_RESULT = 40


def save_test_user(name, email, password) -> User:
    user = User.objects.create_user(username=name, email=email, password=password)
    return user


def save_test_data(name, sex, age, height, weight) -> User:
    user = save_test_user(TEST_USER_NAME, TEST_EMAIL, TEST_PASSWORD)
    MainPersonData.objects.create(
        person=user,
        name=name,
        sex=sex,
        age=age,
        height=height,
        weight=weight
    )
    return user


class BodyMassIndexTest(TestCase):
    def setUp(self) -> None:
        save_test_data(TEST_USER_NAME, TEST_SEX,
                       TEST_AGE, TEST_HEIGHT, TEST_WEIGHT)

    def test_calculate_body_mass_index(self) -> None:
        user = User.objects.get_by_natural_key(TEST_USER_NAME)
        body_mass_index = BodyMassIndex.objects.get(person=user)
        self.assertEqual(body_mass_index.value, TEST_RESULT)


class MainPersonDataTest(TransactionTestCase):
    def test_constraint(self) -> None:
        with self.assertRaises(IntegrityError):
            save_test_data(TEST_USER_NAME, TEST_SEX,
                           TEST_WRONG_AGE, TEST_HEIGHT,
                           TEST_WEIGHT)


class BodyMassIndexUpdateTest(TransactionTestCase):
    def setUp(self) -> None:
        save_test_data(TEST_USER_NAME, TEST_SEX,
                       TEST_AGE, TEST_HEIGHT, TEST_WEIGHT)

    def update_test(self) -> None:
        user = User.objects.get_by_natural_key(TEST_USER_NAME)
        MainPersonData.objects.filter(user=user).update(
            height=TEST_UPDATE_HEIGHT,
            weight=TEST_UPDATE_WEIGHT
        )
        body_mass_index = BodyMassIndex.objects.get(person=user)
        self.assertEqual(body_mass_index.value, TEST_UPDATE_RESULT)
