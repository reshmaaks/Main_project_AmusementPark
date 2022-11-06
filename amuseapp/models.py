from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

# from django.contrib.auth import get_user_model

# User=get_user_model()

# Create your models here.
class Rides(models.Model):
    name=models.CharField(max_length=250,unique=True)
    #slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    # price=models.DecimalField(max_digits=10,decimal_places=2,default=True)
    # category=models.ForeignKey(Category,on_delete=models.CASCADE)
    # subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product',blank=True)
    #stock=models.CharField(max_length=250,default="null")
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name',)
        verbose_name='Ride'
        verbose_name_plural='Rides'

    def _str_(self):
        return '{}'.format(self.name)
  





class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email,phone, password=None):   
        
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            # is_superuser=is_superuser,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, password, email, **extra_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password, **extra_fields
            )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user
    

class Account(AbstractBaseUser,PermissionsMixin):
    
   
    # role_choices    =(('is_admin','is_admin'),('is_superadmin','is_superadmin'),('None','None'))
    id              = models.AutoField(primary_key=True)
    username        = models.CharField(max_length=100, unique=True)
    first_name      = models.CharField(max_length=100, default='')
    last_name       = models.CharField(max_length=100, default='')
    email           = models.EmailField(max_length=100, unique=True)
    phone           = models.BigIntegerField(default=0)
    is_superuser   = models.BooleanField(default=False)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_staff        = models.BooleanField(default=False)
    is_admin        =models.BooleanField(default=False)
    # is_superuser   = models.BooleanField(default=False)

    objects = MyAccountManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name','phone']
   

    class Meta:
        db_table="home_account"


    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin



class Profile(models.Model):
    user=models.ForeignKey(Account, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg', upload_to='profile')
    def __str__(self):
        return f'{self.user.username} Profile'

