from django.shortcuts import render, redirect
from .forms import WatermarkForm
from .models import WatermarkImage
from PIL import Image, ImageDraw, ImageFont
import os
from django.conf import settings

def add_watermark(image_path, watermark_text):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    
    # Position at bottom-right corner
    text_position = (img.width - 100, img.height - 50)
    draw.text(text_position, watermark_text, fill="red", font=font)

    output_path = os.path.join(settings.MEDIA_ROOT, 'outputs/', os.path.basename(image_path))
    img.save(output_path)
    return 'outputs/' + os.path.basename(image_path)

def upload_image(request):
    if request.method == 'POST':
        form = WatermarkForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()
            image_instance.output_image = add_watermark(image_instance.image.path, image_instance.watermark_text)
            image_instance.save()
            return redirect('result', image_instance.id)
    else:
        form = WatermarkForm()
    
    return render(request, 'watermark/upload.html', {'form': form})

def result(request, image_id):
    image = WatermarkImage.objects.get(id=image_id)
    return render(request, 'watermark/result.html', {'image': image})
