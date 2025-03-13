# Generated by Django 5.1.7 on 2025-03-13 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WatermarkImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('watermark_text', models.CharField(max_length=255)),
                ('output_image', models.ImageField(blank=True, null=True, upload_to='outputs/')),
            ],
        ),
    ]
