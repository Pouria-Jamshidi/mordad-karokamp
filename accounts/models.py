from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


# =================================== Text Choices ===================================
class CityChoices(models.TextChoices):
    '''
    City choices for accounts/User model
    '''
    TEHRAN = ("tehran", "تهران")
    ISFAHAN = ("isfahan", "اصفهان")


class GenderChoices(models.TextChoices):
    '''
    Gender choices for accounts/User model
    '''
    MALE = ("male", "مرد")
    FEMALE = ("female", "زن")


# =================================== Models ===================================
def profile_picture_path(instance, filename):
    '''
    a function to generate a dynamic profile picture path
    :param instance: the User model in accounts application
    :param filename: name of the file
    :return: path to profile picture
    '''
    return f"profile_pictures/{instance.gender}/{instance.username}/{datetime.now().strftime('%Y-%m-%d')}/{filename}"


class User(AbstractUser):
    birthdate = models.DateField(null=True, blank=True, verbose_name='تاریخ تولد')
    bio = models.TextField(null=True, blank=True, verbose_name='درباره من')
    city = models.CharField(max_length=20, choices=CityChoices.choices, default=CityChoices.ISFAHAN,
                            verbose_name='شهر محل زندگی')
    gender = models.CharField(max_length=10, choices=GenderChoices.choices, verbose_name='جنسیت')
    profile_picture = models.ImageField(upload_to=profile_picture_path, null=True, blank=True,
                                        default='profile_picture/avatar.png', verbose_name='عکس پروفایل')
    close_friend = models.ManyToManyField(to='self', blank=True, verbose_name='دوستان نزدیک')

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربر'
