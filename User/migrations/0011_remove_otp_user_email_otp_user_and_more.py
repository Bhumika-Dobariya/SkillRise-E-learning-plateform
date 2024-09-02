# Generated by Django 5.1 on 2024-09-02 10:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_alter_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otp',
            name='user_email',
        ),
        migrations.AddField(
            model_name='otp',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='User.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Customer', 'Customer'), ('BankStaff', 'Bank Staff')], default='Customer', max_length=50),
        ),
    ]
