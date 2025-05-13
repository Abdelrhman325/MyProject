from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()  # تغيير CharField إلى TextField
    image = models.ImageField(upload_to='department/', blank=True, null=True)
    vision = models.TextField()  # تصحيح الإملاء من vission إلى vision
    mission = models.TextField()
    doctors = models.ManyToManyField('users.Staff', related_name='assisting_department', blank=True)
    pdf = models.FileField(upload_to='department/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
     return self.name

class SpecialProgram(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()  # تغيير CharField إلى TextField
    image = models.ImageField(upload_to='mastersprogram/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Masters Program: {self.name}"

class MastersProgram(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()  # تغيير CharField إلى TextField
    image = models.ImageField(upload_to='mastersprogram/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Masters Program: {self.name}"