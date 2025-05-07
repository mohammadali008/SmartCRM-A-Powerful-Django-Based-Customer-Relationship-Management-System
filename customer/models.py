from django.db import models

# Define Customer Model
class Customer(models.Model):
    first_name = models.CharField(max_length=150 , verbose_name="نام")
    last_name = models.CharField(max_length=150 , verbose_name="نام خانوادگی")
    phone_number = models.IntegerField(verbose_name="تلفن همراه")
    date_of_birth = models.DateField(verbose_name="تاریخ تولد")
    email = models.CharField(max_length=80,verbose_name="ایمیل")
    state = models.CharField(max_length=80,verbose_name="استان")
    city = models.CharField(max_length=80,verbose_name="شهر")
    address = models.TextField(verbose_name="آدرس")
    phone = models.IntegerField(verbose_name="تلفن ثابت")
    description = models.TextField(verbose_name="توضیحات")
    relationship = models.TextField(verbose_name="نحوه آشنایی")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




