# Generated by Django 4.1 on 2022-09-05 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_notes_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/'),
        ),
    ]
