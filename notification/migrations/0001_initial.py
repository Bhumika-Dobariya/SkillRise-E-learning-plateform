# Generated by Django 5.1 on 2024-08-13 05:46

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0003_alter_student_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('notification_type', models.CharField(choices=[('course_update', 'Course Update'), ('new_course', 'New Course'), ('payment', 'Payment'), ('reminder', 'Reminder'), ('general', 'General')], max_length=50)),
                ('is_read', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('recipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Notification', to='student.student')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
