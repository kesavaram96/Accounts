from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField, NullBooleanField
# Create your models here.

class User(AbstractUser):
    #phone=models.PhoneNumberField()
    
    SELLER = 'seller'
    BUYER = 'buyer'
    DONAR = 'donar'
    ADMIN = 'admin'
    ROLE = [
        (SELLER, 'seller'),
        (BUYER, 'buyer'),
        (DONAR, 'donar'),
        (ADMIN, 'admin'),
    ]
    ROLE = models.CharField(
        max_length=6,
        choices=ROLE,
        default=BUYER,
    )
    def is_upperclass(self):
        return self.ROLE in {self.SELLER, self.BUYER, self.DONAR, self.ADMIN}
    
    def __str__(self):
        return str(self.username)
    
class seller(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    country=models.CharField(max_length=50,blank=False)
    
    def __str__(self):
        return self.username
    
class Buyer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    country=models.CharField(max_length=50,blank=False)
    
    def __str__(self):
        return self.username
    
class Donar(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    country=models.CharField(max_length=50,blank=False)
    
    def __str__(self):
        return self.username
    
    
class Author(models.Model):
    Name=models.CharField(primary_key=True,max_length=100,blank=False)
    
    def __str__(self):
        return str(self.Name)
    
class Publisher(models.Model):
    Name=models.CharField(primary_key=True,max_length=100,blank=False)
    
    def __str__(self):
        return str(self.Name)
    
class Book(models.Model):
    Name=models.CharField(max_length=100,blank=False)
    ISBN=models.IntegerField()
    Author=models.ManyToManyField(Author)
    PublicationDate=models.DateField()
    PublisherInfo=models.ManyToManyField(Publisher)
    Rating=models.FloatField()
    CopyRightInfo=models.TextField()
    NumberOfCopy=models.IntegerField()
    Caption=models.CharField(max_length=50)
    
    GOOD='good'
    DAMAGED='damaged'
    
    Quality= [
        (GOOD,'good'),
        (DAMAGED,'damaged')
    ]
    Quality_Old=models.CharField(max_length=8,choices=Quality,)
    Quality_New=models.CharField(max_length=8,choices=Quality,)
    
    A5='a5'
    A4='a4'
    A3='a3'
    A2='a2'
    A1='a1'
    B3='b3'
    b5='b5'
    Section_ofSize=[
        (A5,'a5'),
        (A4,'a4'),
        (A3,'a3'),
        (A2,'a2'),
        (A1,'a1'),
        (B3,'b3'),
        (b5,'b5'),
    ]
    Size=models.CharField(max_length=8,choices=Section_ofSize,default=A5)
    Price=models.CharField(max_length=14)
    
    FrontCover=models.ImageField(upload_to=None)
    BackCover=models.ImageField(upload_to=None)
    FirstPage=models.ImageField(upload_to=None)
    Body2nd=models.ImageField(upload_to=None)
    PageInside=models.ImageField(upload_to=None)
    DamagedPart=models.ImageField(upload_to=None)
    
    seller=models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.Name)