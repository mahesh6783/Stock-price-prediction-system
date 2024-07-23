from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    uname=models.CharField(max_length=30)
    uphone=models.CharField(max_length=15)
    uemail=models.EmailField()
    ugender=models.CharField(max_length=15)
    upwd=models.CharField(max_length=15)
    status=models.CharField(max_length=15)

    class Meta:
        db_table='user'

class WebsiteUsage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    usage_time = models.IntegerField()

    class Meta:
        db_table='u_usage'

class Payment(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    uname=models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    class Meta:
        db_table='Payment'


class Admin(models.Model):
    aemail=models.CharField(max_length=30)
    aupwd=models.CharField(max_length=15)    
    class Meta:
        db_table='Admin'

class f_d(models.Model):
    u_id=models.ForeignKey(User, on_delete=models.CASCADE)
    uname=models.CharField(max_length=30 ,default="")
    ufd=models.CharField(max_length=500)
    date = models.DateField()
    time=models.CharField(max_length=20)
    Category=models.CharField(max_length=20 ,default="default_category")
    class Meta:
        db_table='user_fd'

class f_d_reply(models.Model):
    f_id=models.ForeignKey(f_d, on_delete=models.CASCADE)
    user_id=models.IntegerField()
    uname=models.CharField(max_length=30 ,default="")
    ufd=models.CharField(max_length=500)
    date = models.DateField()
    time=models.CharField(max_length=20)
    class Meta:
        db_table='user_fd_reply'


class Project(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    responsible = models.ForeignKey(User, on_delete=models.CASCADE)
    week_number = models.CharField(max_length=2, blank=True)
    end_date = models.DateField()

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        print(self.start_date.isocalendar()[1])
        if self.week_number == "":
            self.week_number = self.start_date.isocalendar()[1]
        super().save(*args, **kwargs)