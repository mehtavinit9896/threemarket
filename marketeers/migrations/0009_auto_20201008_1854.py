# Generated by Django 3.0.3 on 2020-10-08 13:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('marketeers', '0008_auto_20201005_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='image',
            field=models.FileField(upload_to='marketeers\\static\\marketeers\\images\\Client'),
        ),
        migrations.AlterField(
            model_name='event',
            name='desc',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.FileField(upload_to='marketeers\\static\\marketeers\\images\\Events'),
        ),
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.FileField(upload_to='marketeers\\static\\marketeers\\images\\Team'),
        ),
    ]
