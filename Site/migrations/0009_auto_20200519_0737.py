# Generated by Django 3.0.4 on 2020-05-19 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0008_auto_20200518_1344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comments',
            new_name='text',
        ),
    ]
