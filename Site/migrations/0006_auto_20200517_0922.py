# Generated by Django 3.0.4 on 2020-05-17 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0005_auto_20200516_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='media/default.jpg', upload_to=''),
        ),
    ]