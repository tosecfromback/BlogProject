from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone

# Create your models here.

class UserManager(BaseUserManager):

    def _create_user(self, id, password, email, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError("User must have an E-mail")
        now = timezone.localtime()
        email = self.normalize_email(email)
        user = self.model(
            id = id,
            is_staff = is_staff,
            is_superuser = is_superuser,
            last_login = now,
            date_joined = now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, id, email, password, **extra_fields):
        return self._create_user(id, email, password, False, False, **extra_fields)
    
    def create_superuser(self, id, email, password, **extra_fields):
        return self._create_user(id, email, password, True, True, **extra_fields)
    

class User(AbstractUser):
    username = None
    id = models.CharField(unique=True, max_length=155)
    email = models.EmailField(unique=True, max_length=155)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'id'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()