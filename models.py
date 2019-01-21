from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.


class Task(models.Model):
    class Meta:
        verbose_name = '작업'
        verbose_name_plural = '작업'
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='작성자', related_name='author')
    director = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='담당 디렉터', related_name='director')
    description = models.CharField(max_length=300, verbose_name='설명')
    archive = models.BooleanField(default=False, verbose_name='아카이브 여부')
    timestamp = models.DateTimeField(default=timezone.now, verbose_name='생성된 날짜')


class Project(models.Model):
    class Meta:
        verbose_name = '프로젝트'
        verbose_name_plural = '프로젝트'
    name = models.CharField(max_length=30, verbose_name='프로젝트 이름')
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='관리자', related_name='manager')
    directors = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='참여 디렉터들', related_name='directors')
    archive = models.BooleanField(default=False, verbose_name='아카이브 여부')
    timestamp = models.DateTimeField(default=timezone.now, verbose_name='생성된 날짜')
