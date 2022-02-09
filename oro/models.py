from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=22)
    img = models.ImageField(upload_to ='', default='https://media.istockphoto.com/photos/pop-it-pikachu-pokemon-on-dark-background-picture-id1339486581')
    # connecting the item to a User, CASCADE deletes any item associated with User
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null= True)

    # make sure the object in the database reflects its name
    def __str__(self):
        return self.name