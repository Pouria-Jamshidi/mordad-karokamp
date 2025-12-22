from django.db import models
from datetime import datetime
from accounts.models import User

# =================================== Text Choices ===================================
class ShowToChoices(models.TextChoices):
    NOBODY = ("nobody", "هیچکس")
    CLOSEFRIENDS = ("closefriends", "دوستان صمیمی")
    ALL = ("all", "همه")


class CategoryChoices(models.TextChoices):
    SOCIAL = ("social", "اجتماعی")
    SPORT = ("sport", "ورزشی")

# =================================== Models ===================================
def post_picture_path(instance, filename):
    '''
    a function to generate a dynamic post picture path
    :param instance: the User model in accounts application
    :param filename: name of the file
    :return: path to post picture
    '''
    return f"profile_pictures/{datetime.now().strftime('%Y%m%d')}/{instance.user.username}/{instance.id}/{filename}"

class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name='تیتر')
    content = models.TextField(verbose_name='محتوا')
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, verbose_name='کاربر',related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت پست')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آخرین زمان تغییرات پست')
    visible = models.BooleanField(default=False, verbose_name='قابل رویت بودن')
    show_to = models.CharField(
        max_length=20, choices=ShowToChoices.choices, default=ShowToChoices.NOBODY, verbose_name='مشاهده به'
    )
    is_deleted = models.BooleanField(default=False, verbose_name='حذف شده')
    category = models.CharField(max_length=20, choices=CategoryChoices, verbose_name='دسته بندی')
    image = models.ImageField(upload_to=post_picture_path, null=True, blank=True,verbose_name='اپلود عکس')

    def has_image(self):
        if self.image:
            return True
        return False

    def __str__(self):
        return f"{self.title}:   {self.content}"

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست"
