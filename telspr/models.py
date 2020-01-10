from django.db import models

# Create your models here.

class Person(models.Model):
    surname = models.CharField(max_length=50,verbose_name='Фамилия')
    first_name = models.CharField(max_length=50,verbose_name='Имя')
    second_name = models.CharField(max_length=50,verbose_name='Отчество')
    mgts = models.CharField(null=True,blank=True,max_length=50,verbose_name='МГТС')
    ats_ogv = models.CharField(null=True,blank=True,max_length=10,verbose_name='АТС-ОГВ')
    mestniy = models.CharField(null=True,blank=True,max_length=10,verbose_name='Мест')
    room =  models.CharField(null=True,blank=True,max_length=10,verbose_name='Кабинет')
    gate =  models.CharField(null=True,blank=True,max_length=10,verbose_name='Подъезд')
    otdel = models.CharField(null=True,blank=True,max_length=10,verbose_name='Отдел')

    class Meta:
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'
