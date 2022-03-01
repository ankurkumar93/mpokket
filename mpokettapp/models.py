from operator import mod
from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    email = models.EmailField()
    mobile = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    
    db_table = 'tbl_users'