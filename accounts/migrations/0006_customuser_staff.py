# Generated by Django 3.2.16 on 2023-02-10 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_customuser_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='staff',
            field=models.BooleanField(default=False),
        ),
    ]