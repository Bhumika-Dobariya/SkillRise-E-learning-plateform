# Generated by Django 5.1 on 2024-08-09 05:32

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Course', '0005_studentcourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('chapter', models.PositiveIntegerField()),
                ('content', models.TextField(blank=True, null=True)),
                ('video_url', models.URLField(blank=True, null=True)),
                ('quiz_url', models.URLField(blank=True, null=True)),
                ('assignment_url', models.URLField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='Course.course')),
            ],
            options={
                'ordering': ['chapter'],
            },
        ),
    ]
