from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    rollNo = models.IntegerField(default=111111)
    fathersName = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
class Category(models.Model):
    category = models.CharField(max_length = 20)
    def __str__(self) -> str:
        return self.category
    
class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE )
    book = models.CharField(max_length=20 )

    def __str__(self) -> str:
        return self.book