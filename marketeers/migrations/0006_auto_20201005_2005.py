# Generated by Django 3.0.3 on 2020-10-05 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketeers', '0005_auto_20201005_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.FileField(upload_to='\\static\\marketeers\\images\\Events'),
        ),
    ]
