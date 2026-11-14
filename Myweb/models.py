from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Profile(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')
    job_title = models.CharField(max_length=50, verbose_name='عنوان شعل')
    intro_text = models.TextField(verbose_name='متن کوتاه معرفی در هدر')
    about_text = models.Textfield(verbose_name='درباره ی من')
    birth_date = models.CharField(max_length=50, verbose_name='تاریخ تولد ', default='1389/12/22')
    phone = models.CharField(max_length=30, verbose_name='شماره تماس')
    email = models.EmailField(verbose_name='ادرس ایمیل')
    address = models.CharField(max_length=200, verbose_name='ادرس و محل سکونت')
    avatar = models.ImageField(upload_to='profile/', null=True, blank=True, verbose_name="یلنسرپ سکع")
    resume_file = models.FileField(upload_to='resumes/', null=True, blank=True, verbose_name="هم فایل رزوPD")
    budget = models.CharField(max_length=50, default='250,000 ت', verbose_name='بودجه مالی')
    total_projects = models.PositiveIntegerField(default=120, verbose_name='تعداد پروژه ما')
    happy_clients = models.PositiveIntegerField(default=85, verbose_name='یض')

class Meta:
    verbose_name='پروفایل شخصی'
    verbose_name_plural ='پروفایل شخصی'

    def __str__(self):
        return self.full_name


class skill(models.Model):
    title = models.CharField(max_length=80, verbose_name='عنوان مهارت')
    percentage = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        verbose_name='درصد تسلط(1 تا 100)')
    
order = models.PositiveIntegerField(default=0, verbose_name='ترتیب نمایش')


class Meta:
    verbose_name ='مهارت'
    verbose_name_plural ='مهارت ها'
    ordering = ['order', '-percentage']

    def __str__(self):
        return f"{self.title} ({self.percentage}%)


class Experience(models.Model):
    company = models.CharField(max_length=120, verbose_name='مجموعه')
    role = models.CharField(max_length=120, verbose_name='عنوان شغلی')
    location = models.CharField(max_length=100, verbose_name='موقعیت مکانی', default = 'گرگان , فارس')
    date_range = models.CharField(max_length=80, verbose_name='بازه زمانی')
    description = models.TextField(blank=True, verbose_name='توضیحات و دستاورد ها')