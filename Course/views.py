from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Course,StudentCourse
from .serializer import CourseSerializer,StudentCourseSerializer
from instructor.models import Instructor


########################## add student to course #############################


@api_view(["POST"])
def add_student_to_course(request):
    serializer = StudentCourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_student_course_by_id(request):
    student_course_id = request.query_params.get('id')

    if not student_course_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    student_course = StudentCourse.objects.filter(id=student_course_id, is_active=True, is_deleted=False).first()

    if not student_course:
        return Response({"error": "StudentCourse not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = StudentCourseSerializer(student_course)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])

def get_students_by_course(request):
    course_id = request.query_params.get('course_id')

    if not course_id:
        return Response({"error": "course_id query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    student_courses = StudentCourse.objects.filter(course_id=course_id, is_active=True, is_deleted=False)

    if not student_courses.exists():
        return Response({"error": "No students found for this course"}, status=status.HTTP_404_NOT_FOUND)

    serializer = StudentCourseSerializer(student_courses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def get_all_student_courses(request):
    student_courses = StudentCourse.objects.filter(is_active=True, is_deleted=False)
    serializer = StudentCourseSerializer(student_courses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['PUT'])
def update_student_course(request):
    course_id = request.query_params.get('id')

    if not course_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    student_course = StudentCourse.objects.filter(id=course_id).first()

    if not student_course:
        return Response({"error": "StudentCourse not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = StudentCourseSerializer(student_course, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_student_course(request):
    course_id = request.query_params.get('id')

    if not course_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    student_course = StudentCourse.objects.filter(id=course_id).first()

    if not student_course:
        return Response({"error": "StudentCourse not found"}, status=status.HTTP_404_NOT_FOUND)

    student_course.delete()
    return Response({"message": "StudentCourse deleted successfully"}, status=status.HTTP_204_NO_CONTENT)




################################### course ########################################



#_____________ create course ________________

@api_view(["POST"])
def create_course(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
     
        data = serializer.validated_data
        price = data.get('price')
        discount_percent = data.get('discount_percent')

       
        if discount_percent is not None:
            cal_discount = (price * discount_percent) / 100
            discount_price = price - cal_discount
        else:
            discount_price = price
        
        course = serializer.save(discount_price=discount_price)
        
        return Response(CourseSerializer(course).data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#___________ get course by id _________________

@api_view(['GET'])
def get_course_by_id(request):
    course_id = request.query_params.get('id')

    if not course_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    course = Course.objects.filter(id=course_id).first()

    if not course:
        return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CourseSerializer(course)
    return Response(serializer.data, status=status.HTTP_200_OK)



#________________ get all courses ___________________

@api_view(["GET"])
def get_all_courses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



#______________update course _________________

@api_view(["PUT"])
def update_course(request):
  
    course_id = request.query_params.get('id')
    
    if not course_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    course = Course.objects.filter(pk=course_id).first()
    
    if not course:
        return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CourseSerializer(course, data=request.data, partial=True)
    if serializer.is_valid():
        data = serializer.validated_data
        price = data.get('price')
        discount_percent = data.get('discount_percent')

        if discount_percent is not None:
            cal_discount = (price * discount_percent) / 100
            discount_price = price - cal_discount
            serializer.validated_data['discount_price'] = discount_price

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#________________ delete course ______________________

@api_view(["DELETE"])
def delete_course(request):
    course_id = request.query_params.get('id')
    
    if not course_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    course = Course.objects.filter(pk=course_id).first()
    
    if not course:
        return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

    course.delete()
    
    return Response({"message": "Course deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



#__________________get courses by category__________________

@api_view(['GET'])
def get_courses_by_category(request):
    category_id = request.query_params.get('category_id')

    if not category_id:
        return Response({"error": "Category ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    courses = Course.objects.filter(category_id=category_id)

    if not courses.exists():
        return Response({"error": "No courses found for this category"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


#_______________get course by instructor_________________

@api_view(['GET'])
def get_courses_by_instructor(request):
    instructor_id = request.query_params.get('instructor_id')

    if not instructor_id:
        return Response({"error": "Instructor ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    instructor = Instructor.objects.filter(id=instructor_id).first()

    if not instructor:
        return Response({"error": "Instructor not found"}, status=status.HTTP_404_NOT_FOUND)

    courses = Course.objects.filter(instructor=instructor)

    course_names = courses.values_list('name', flat=True)
    return Response(course_names, status=status.HTTP_200_OK)