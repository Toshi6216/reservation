# Generated by Django 3.2.16 on 2023-02-23 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservation', '0015_auto_20230223_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovedStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveConstraint(
            model_name='approvedmember',
            name='approved_unique',
        ),
        migrations.RenameField(
            model_name='approvedmember',
            old_name='approved_member',
            new_name='member',
        ),
        migrations.AddConstraint(
            model_name='approvedmember',
            constraint=models.UniqueConstraint(fields=('member', 'group'), name='approved_member_unique'),
        ),
        migrations.AddField(
            model_name='approvedstaff',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.group'),
        ),
        migrations.AddField(
            model_name='approvedstaff',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='approvedstaff',
            constraint=models.UniqueConstraint(fields=('staff', 'group'), name='approved_staff_unique'),
        ),
    ]
