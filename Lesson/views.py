from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import LessonSerializer
from  .models import Lesson
from datetime import datetime
from datetime import timedelta



@api_view(["POST"])
def create_lesson(request):
    data = request.data
    serializer = LessonSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def get_lesson_by_id(request):
    lesson_id = request.query_params.get('id')
    
    if not lesson_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    lesson = Lesson.objects.filter(pk=lesson_id).first()
    
    if not lesson:
        return Response({"error": "Lesson not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = LessonSerializer(lesson)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_all_lessons(request):
    lessons = Lesson.objects.all()
    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(["PUT"])
def update_lesson(request):
    lesson_id = request.query_params.get('id')
    
    if not lesson_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    lesson = Lesson.objects.filter(pk=lesson_id).first()
    
    if not lesson:
        return Response({"error": "Lesson not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = LessonSerializer(lesson, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(["DELETE"])
def delete_lesson(request):
    lesson_id = request.query_params.get('id')
    
    if not lesson_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    lesson = Lesson.objects.filter(pk=lesson_id).first()
    
    if not lesson:
        return Response({"error": "Lesson not found"}, status=status.HTTP_404_NOT_FOUND)
    
    lesson.delete()
    
    
    
@api_view(["GET"])
def get_lessons_by_module(request):
    module_id = request.query_params.get('module_id')
    
    if not module_id:
        return Response({"error": "Module ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    lessons = Lesson.objects.filter(module_id=module_id)
    
    if not lessons.exists():
        return Response({"error": "No lessons found for this module"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_lessons_by_chapter(request):
    chapter = request.query_params.get('chapter')
    
    if not chapter:
        return Response({"error": "Chapter query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    lessons = Lesson.objects.filter(chapter=chapter)
    
    if not lessons.exists():
        return Response({"error": "No lessons found for this chapter"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_active_lessons(request):
    lessons = Lesson.objects.filter(is_active=True)
    
    if not lessons.exists():
        return Response({"error": "No active lessons found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(["GET"])
def get_lessons_by_duration(request):
    min_duration_str = request.query_params.get('min_duration')
    max_duration_str = request.query_params.get('max_duration')

    if not min_duration_str or not max_duration_str:
        return Response({"error": "Both min_duration and max_duration query parameters are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        min_duration = parse_duration(min_duration_str)
        max_duration = parse_duration(max_duration_str)
    except ValueError:
        return Response({"error": "Invalid duration format"}, status=status.HTTP_400_BAD_REQUEST)

    lessons = Lesson.objects.filter(duration__gte=min_duration, duration__lte=max_duration)

    if not lessons.exists():
        return Response({"error": "No lessons found within this duration range"}, status=status.HTTP_404_NOT_FOUND)

    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def parse_duration(duration_str):
    """Convert a duration string in HH:MM:SS format to a timedelta object."""
    try:
        hours, minutes, seconds = map(int, duration_str.split(':'))
        return timedelta(hours=hours, minutes=minutes, seconds=seconds)
    except ValueError:
        raise ValueError("Invalid duration format. Expected HH:MM:SS.")



@api_view(["GET"])
def get_lessons_by_date_range(request):
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')

    if not start_date or not end_date:
        return Response({"error": "Both start_date and end_date query parameters are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        return Response({"error": "Invalid date format, use YYYY-MM-DD"}, status=status.HTTP_400_BAD_REQUEST)

    lessons = Lesson.objects.filter(created_at__range=[start_date, end_date])

    if not lessons.exists():
        return Response({"error": "No lessons found within this date range"}, status=status.HTTP_404_NOT_FOUND)

    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)