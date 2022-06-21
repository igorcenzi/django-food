from django.db import models

# Create your models here.
class Address(models.Model):
  street = models.CharField(max_length=50)
  number = models.IntegerField()
  complement = models.CharField(max_length=40, null=True)

  user = models.OneToOneField('users.User', on_delete=models.CASCADE)
  
  def __repr__(self):
    return f'Address {self.id} - {self.street}/{self.number}'