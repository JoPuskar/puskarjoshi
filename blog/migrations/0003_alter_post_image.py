# Generated by Django 4.1.6 on 2023-03-03 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/images', default='blog/images/Puskar1.jpg'),
        ),
    ]
