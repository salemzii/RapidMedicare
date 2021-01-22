from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateField(timezone.now)

    def __str__(self):
        return self.title



class Comment(models.Model):
    name = models.CharField(max_length=50)
    comment = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class meta:
        ordering = ['date']

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150)
    verified = models.BooleanField(default=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    is_hospital = models.BooleanField(default= False) 
    location = models.CharField(max_length=101, default='Nigeria', blank= True, null= True)
    phoneNumber = models.CharField(max_length=11, default= 123, blank= True, null= True)
    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class HospitalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description= models.TextField(default="No description", blank= True, null= True)
    ValidDoc = models.ImageField(default = 'Document.png', upload_to='Documents')
    Frontview = models.ImageField(default='Hospital.jpg', upload_to='Hospital_pics')
    Backview = models.ImageField(default='Hospital.jpg', upload_to='Hospital_pics')



    def __str__(self):
        return f"{self.user.username}'s Hospital Information"