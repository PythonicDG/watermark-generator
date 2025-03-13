from django.db import models

class WatermarkImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    watermark_text = models.CharField(max_length=255)
    output_image = models.ImageField(upload_to='outputs/', blank=True, null=True)

    def __str__(self):
        return self.watermark_text
