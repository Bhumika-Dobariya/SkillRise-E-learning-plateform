# Generated by Django 5.1 on 2024-08-12 05:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_blacklistedtoken_rename_last_login_user_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
