from django.db import models
#from django.contrib.auth.models import User
#Email = email.objects.get(id=mail_id)

#payment.mail = Email
# Create your models here.
class user(models.Model):
   
    name=models.CharField(max_length=50)
    email=models.EmailField(primary_key = True,max_length=50)
    password=models.CharField(max_length=50)
    age=models.IntegerField(default=0)

'''class gym(models.Model):
    gymid=models.IntegerField(primary_key = True)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=150)
    rating=models.IntegerField(default=0)
    description=models.CharField(max_length=250)

class accessories(models.Model):
    itemid=models.IntegerField(default=0)
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    description=models.CharField(max_length=250)

class trainers(models.Model):
    trainerid=models.IntegerField(primary_key = True)
    gymid=models.ForeignKey(gym, on_delete=models.PROTECT)
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    rating=models.IntegerField(default=0)
    description=models.CharField(max_length=250)


class equipments(models.Model):
    itemid=models.IntegerField(default=0)
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    description=models.CharField(max_length=250)

class nutrition(models.Model):
    itemid=models.IntegerField(default=0)
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    description=models.CharField(max_length=250)'''

class payment(models.Model):
    name = models.CharField(max_length=50)
    tamount=models.IntegerField(default=0)
    quantity=models.IntegerField(default=0)
    address = models.CharField(max_length=50)
    date=models.CharField(max_length=20)
    email=models.ForeignKey(user,to_field="email", on_delete=models.CASCADE)

'''class transaction(models.Model):
    name = models.CharField(max_length=50)
    amount=models.IntegerField(default=0)'''
    