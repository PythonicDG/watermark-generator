import os
from django.conf import settings
from django.shortcuts import render
from .forms import UploadImageForm
from .models import WatermarkImage
from PIL import Image, ImageDraw, ImageFont

def add_watermark(image_path, text):
    """ Adds a watermark with user-input text """
    output_folder = os.path.join(settings.MEDIA_ROOT, 'outputs')
    os.makedirs(output_folder, exist_ok=True)  # Ensure folder exists

    image = Image.open(image_path).convert("RGBA")
    width, height = image.size

    # Create a transparent overlay for the watermark
    watermark = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(watermark)

    try:
        font = ImageFont.truetype("arial.ttf", 36)  # Adjust font size as needed
    except IOError:
        font = ImageFont.load_default()

    # Get text width and height using textbbox()
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

    text_position = (width - text_width - 20, height - text_height - 20)  # Bottom-right corner

    draw.text(text_position, text, fill=(255, 255, 255, 128), font=font)

    watermarked_image = Image.alpha_composite(image, watermark)
    output_path = os.path.join(output_folder, os.path.basename(image_path))
    watermarked_image.convert("RGB").save(output_path)

    return output_path.replace(settings.MEDIA_ROOT, '')

def upload_image(request):
    """ Handles image upload and applies watermark with custom text """
    if request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = WatermarkImage(image=form.cleaned_data['image'])
            image_instance.save()

            # Get user-input watermark text
            watermark_text = form.cleaned_data['text']
            image_path = image_instance.image.path  # Get full file path

            # Apply watermark with custom text
            watermarked_path = add_watermark(image_path, watermark_text)

            # Save the new watermarked image path
            image_instance.watermarked_image = watermarked_path
            image_instance.save()

            return render(request, 'watermark/result.html', {'image': image_instance, 'text': watermark_text})

    else:
        form = UploadImageForm()

    return render(request, 'watermark/upload.html', {'form': form})
