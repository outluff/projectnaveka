from django.db import models


class Course(models.Model):
    title = models.CharField('Курсы', max_length = 50)
    course = models.TextField('Описание')

    def __str__(self):
        return self.title


class User(models.Model):
    fio = models.CharField('Юзеры', max_length = 50)
    user = models.TextField('Инфо')

    def __str__(self):
        return self.fio
