# Generated by Django 4.1 on 2022-09-02 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LogIn',
        ),
        migrations.DeleteModel(
            name='SignUp',
        ),
    ]
