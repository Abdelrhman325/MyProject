from django.db import models

class unit(models.Model):

 
    name = models.CharField(max_length=255, unique=True, )
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='Unites/', blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    speech = models.TextField(blank=True, null=True)
    biography_link = models.URLField(blank=True, null=True)
    organizational_structure = models.ImageField(upload_to='Unites/structure/', blank=True, null=True)
    page= models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
def __str__(self):
    return getattr(self, 'name', 'Unnamed Unit')



class UnitService(models.Model):
    unit = models.ForeignKey(unit, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    page= models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.unit.name}"