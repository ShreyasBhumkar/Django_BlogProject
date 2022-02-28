from django.db import models
from django.contrib.auth.models import User

class Add_Blog(models.Model):
    Blog_Title = models.CharField(max_length=200)
    Blog_Body = models.TextField()
    Date_Posted = models.DateField(auto_now_add=True)
    Blog_Image = models.ImageField(upload_to = 'images/', blank=True, null=True)
    User_Name = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Blog_Title