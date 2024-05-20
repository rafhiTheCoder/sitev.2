from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Serra(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="serra" ,null=True)
    code = models.CharField(max_length=200)

    def __str__(self):
        return self.code
    
