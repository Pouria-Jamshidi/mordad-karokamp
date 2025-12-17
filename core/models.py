from django.db import models


class CityChoices(models.TextChoices):
    TEHRAN = ("tehran", "تهران")
    ISFAHAN = ("isfahan", "اصفهان")


class ShowToChoices(models.TextChoices):
    NOBODY = ("nobody", "هیچکس")
    CLOSEFRIENDS = ("closefriends", "دوستان صمیمی")
    ALL = ("all", "همه")


class GenderChoices(models.TextChoices):
    MALE = ("male", "مرد")
    FEMALE = ("female", "زن")


class CategoryChoices(models.TextChoices):
    SOCIAL = ("social", "اجتماعی")
    SPORT = ("sport", "ورزشی")


class User(models.Model):
    username = models.CharField(max_length=32, unique=True, verbose_name="نام کاربری")
    password = models.CharField(max_length=20, verbose_name="رمز ورود")
    birthdate = models.DateField(null=True, verbose_name="تاریخ تولد")
    bio = models.TextField(null=True, verbose_name='درباره من', blank=True)
    city = models.CharField(
        max_length=20, choices=CityChoices.choices, default=CityChoices.ISFAHAN, verbose_name='شهر محل زندگی'
    )
    email = models.EmailField("ایمیل")
    close_friend = models.ManyToManyField(to="self", null=True, blank=True, verbose_name='دوستان نزدیک')

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر"


admin_user = User.objects.filter(username="admin").first()


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name='تیتر')
    content = models.TextField(verbose_name='محتوا')
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, verbose_name='کاربر')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت پست')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آخرین زمان تغییرات پست')
    visible = models.BooleanField(default=False, verbose_name='قابل رویت بودن')
    show_to = models.CharField(
        max_length=20, choices=ShowToChoices.choices, default=ShowToChoices.NOBODY, verbose_name='مشاهده به'
    )
    is_deleted = models.BooleanField(default=False, verbose_name='حذف شده')
    category = models.CharField(max_length=20, choices=CategoryChoices, verbose_name='دسته بندی')
    image = models.ImageField(upload_to='post_pictures', null=True, blank=True)

    def __str__(self):
        return f"{self.title}:   {self.content}"

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست"
