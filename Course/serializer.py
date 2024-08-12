from rest_framework import serializers 
from .models import Course,StudentCourse
from category.models import Category
from instructor.models import Instructor
from student.models import Student



class CourseSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    instructor = serializers.PrimaryKeyRelatedField(queryset=Instructor.objects.all())
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())

    class Meta:
        model = Course
        fields = [
            'id', 'category', 'instructor', 'student', 'name', 'description',
            'duration', 'start_date', 'end_date', 'level', 'price', 'discount_price',
            'discount_percent', 'language', 'is_published', 'rating', 'is_active', 'created_at', 'updated_at'
        ]



class StudentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourse
        fields = ['id', 'course', 'student', 'created_at', 'modified_at', 'is_active', 'is_deleted']
      