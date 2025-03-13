from django import forms
from .models import WatermarkImage

class WatermarkForm(forms.ModelForm):
    class Meta:
        model = WatermarkImage
        fields = ['image', 'watermark_text']
