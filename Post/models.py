from django.db import models
from phone_field import PhoneField
from django.core.validators import RegexValidator
# Create your models here.


class Post(models.Model):
    Name = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{10}$', message="Phone number must be 10 digits and  entered in the format: '98XXXXXXXX'.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=13)  # validators should be a list
    url_location = models.URLField(max_length=200, null=True)
    amount = models.IntegerField(null=True)
    length = models.IntegerField(null=True)
    breadth = models.IntegerField(null=True)
    image1 = models.ImageField(upload_to='images/', default=True)
    image2 = models.ImageField(upload_to='images/', default=True)
    image3 = models.ImageField(upload_to='images/', default=True)
    image4 = models.ImageField(upload_to='images/', default=True)

    def __str__(self):
        return self.Name
