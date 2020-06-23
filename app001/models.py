from django.db import models

# Create your models here.

#出版社
class Publisher(models.Model):
    #自增的ID主键
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=64,null=False,unique=True)
#书
class Book(models.Model):
    id=models.AutoField(primary_key=True)
    #创建一个varchar(64)的唯一不为空的字段
    title=models.CharField(max_length=64,null=False,unique=True)
    #和出版社关联的字段
    publisher=models.ForeignKey(to=Publisher)
#作者
class Author(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=16,null=False,unique=True)
    book=models.ManyToManyField(to=Book)
