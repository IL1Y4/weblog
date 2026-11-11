from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Profile(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')
    job_title = models.CharField(max_length=50, verbose_name='عنوان شعل')
    intro_text = models.Textfield(verbose_name='متن کوتاه معرفی در هدر')
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