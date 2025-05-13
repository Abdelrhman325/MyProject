from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    USER_TYPE_CHOICES = (
        ('graduation', 'Graduation'),
        ('', 'None'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, blank=True, default='')
    username = models.CharField(max_length=150)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'  # ← دي هنا
    REQUIRED_FIELDS = ['username']  # ← دي هنا برضه


    def __str__(self):
        return self.email
    

class Graduation(models.Model):
    EMPLOYMENT_CHOICES = [
        ('employee', 'Employee'),
        ('unemployee', 'Unemployee'),
        ('freelance', 'Freelance'),
        ('postgraduate', 'Postgraduate Studies'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='graduation_info')
    cv = models.FileField(upload_to='cvs/')
    employment_status = models.CharField(max_length=100, choices=EMPLOYMENT_CHOICES)
    job_name = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    company_email = models.EmailField(blank=True)
    company_phone = models.CharField(max_length=20, blank=True)
    company_link = models.URLField(blank=True)
    about_company = models.TextField(blank=True)

    def __str__(self):
        return f"Graduation Info for {self.user.username}"




class Staff(models.Model):
    name= models.CharField(max_length=100)
    position= models.CharField(max_length=100)
    cv= models.FileField(upload_to='staff_cvs/', blank=True, null=True)
    image= models.ImageField(upload_to='staff_images/', blank=True, null=True)
    department=models.ManyToManyField('academics.Department', blank=True, related_name='staffs')

    def __str__(self):
     return f"Staff Member: {self.name}, Position: {self.position}"
