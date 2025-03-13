from django import forms
from .models import WatermarkImage

class UploadImageForm(forms.ModelForm):
    text = forms.CharField(max_length=50, required=True, label="Watermark Text")

    class Meta:
        model = WatermarkImage
        fields = ['image', 'text']
