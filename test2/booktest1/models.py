from django.db import models
# 与数据库进行交互
# Create your models here.

class Book( models.Model ):
    book_name = models.CharField( max_length=20 )
    book_date = models.DateField()

    def __str__(self):
        return self.book_name


class Hero( models.Model ):
    hero_name = models.CharField(max_length=20)
    hero_skill = models.CharField(max_length=128)
    book_id = models.ForeignKey( 'Book', on_delete=models.CASCADE, )

    def __str__(self):
        return self.hero_name