from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    content = models.TextField(max_length=500)
    def __str__(self) -> str:
        return 'Message From '+ self.name +' Email ID - ' + self.email 