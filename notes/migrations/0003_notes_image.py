# Generated by Django 4.1 on 2022-09-02 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_notes_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='image',
            field=models.ImageField(null=True, upload_to='static/'),
        ),
    ]
