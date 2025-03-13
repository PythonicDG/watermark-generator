from django.db import models

class WatermarkImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    watermarked_image = models.ImageField(upload_to='outputs/', blank=True, null=True)

    def __str__(self):
        return self.image.name
