from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializer import StudentSerializer



# Create a new student

@api_view(["POST"])

def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# Get a student by ID

@api_view(['GET'])
def get_student_by_id(request):
    student_id = request.query_params.get('id') 
    
    if not student_id:
        return Response({"error": "ID parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = StudentSerializer(student)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Get all students

@api_view(["GET"])
def get_all_students(request):
    students = Student.objects.filter(is_deleted=False)
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



# Update student information
@api_view(['PUT'])
def update_student(request):
    student_id = request.query_params.get('id')  
    
    if not student_id:
        return Response({"error": "ID parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
    
    student = Student.objects.filter(id=student_id, is_deleted=False).first()
    if student is None:
        return Response({"detail": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = StudentSerializer(student, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete a student


@api_view(["DELETE"])
def delete_student(request):
  
    id = request.query_params.get('id')
    if not id:
        return Response({"detail": "ID parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    student = Student.objects.filter(id=id, is_deleted=False).first()
    if student is None:
        return Response({"detail": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
    
    student.is_deleted = True
    student.save()
    return Response({"message": "Student marked as deleted"}, status=status.HTTP_204_NO_CONTENT)




@api_view(["GET"])
def list_students_with_filters(request):
    status_filter = request.query_params.get('status', None)
    if status_filter:
        students = Student.objects.filter(is_deleted=False, is_active=status_filter)
    else:
        students = Student.objects.filter(is_deleted=False)
    
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)





@api_view(["GET"])
def get_students_by_gender(request):
    gender = request.query_params.get('gender', None)
    
    if gender not in dict(Student.GENDER_CHOICES).keys():
        return Response({"detail": "Invalid gender"}, status=status.HTTP_400_BAD_REQUEST)

    students = Student.objects.filter(gender=gender, is_deleted=False)
    if not students.exists():
        return Response({"detail": "No students found for this gender"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)