from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
'''دستهبندی مقالات وبلاگ'''
title = models.CharField(max_length=100, verbose_name='عنوان دسته بندی')
slug = models.SlugField(max_length=120, unique=True, allow_unicode=True, verbose_name='اسلاگ')


class Meta:
    verbose_name = 'دسته بندی'
    verbose_name_plural = 'دسته بندی وبلاگ'


    def __str__(self):
        return self.title

class Post(models.Model):
'''مدل مقالات وبلاگ'''
    title = models.CharField(max_length=200, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=220, unique=True, allow_unicode=True, verbose_name='اسلاگ مقاله')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='نویسنده')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts', verbo)
    image = models.ImageField(upload_to='blog/', verbose_name='تصویر شاخص مقاله')
    summary = models.TextField(max_length=350, verbose_name='خلاصه کوتاه مقاله')
    content = models.TextField(verbose_name='متن کامل مفاله')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'تاریخ انتشار')
    views_count = models.PositiveIntegerField(default=0, verbose_name ='تعداد بازدید')
    is_published = models.BooleanField(default=True, verbose_name='منتشر شده؟')



class Meta:
verbose_name = 'مقاله'
verbose_name_plural = 'مقالات وبلاگ'
ordering = ['-created_at']


    def __str__(self):
        return self.title


class Comment(models.Model):
'''مدل نظرات کاربران برای هر مقاله'''
post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='مقاله مرتبط ')
name = models.CharField(max_length=100, verbose_name='نام کاربر')
email = models.EmailField(verbose_name='ایمیل کاربر')
message = models.TextField(verbose_name = 'متن نظر')
created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال')
is_approved = models.BooleanField(default=False, verbose_name = 'ارسال شده؟')
