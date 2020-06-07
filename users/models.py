from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='images/profile_pictures')
    bio = models.TextField(blank=True, default="")

    def __str__(self):
        return f'{self.user.username}\'s profile'

    def save(self):
        img = Image.open(self.image.path)
        if img.height > 300 and img.width > 300:
            # create image thumbnails
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)