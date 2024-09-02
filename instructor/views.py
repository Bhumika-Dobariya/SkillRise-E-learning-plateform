from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Instructor
from .serializer import InstructorSerializer






#___________________create instructor_________________

@api_view(["POST"])
def create_instructor(request):
    data = request.data
    serializer = InstructorSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#_________________get instructor by id ________________

@api_view(["GET"])
def get_instructor_by_id(request):
    id = request.query_params.get('id')
    
    if not id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    instructor = Instructor.objects.filter(pk=id).first()
    
    if not instructor:
        return Response({"error": "Instructor not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = InstructorSerializer(instructor)
    return Response(serializer.data, status=status.HTTP_200_OK)


#___________get all instructor_________________

@api_view(["GET"])
def get_all_instructors(request):
    instructors = Instructor.objects.all()
    serializer = InstructorSerializer(instructors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



#______________update instructor______________

@api_view(["PUT"])
def update_instructor(request):
    
    id = request.query_params.get('id')
    
    if not id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    instructor = Instructor.objects.filter(pk=id).first()
    
    if not instructor:
        return Response({"error": "Instructor not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = InstructorSerializer(instructor, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#______________delete instructor _________________

@api_view(["DELETE"])
def delete_instructor(request):
    id = request.query_params.get('id')
    
    if not id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    instructor = Instructor.objects.filter(pk=id).first()
    
    if not instructor:
        return Response({"error": "Instructor not found"}, status=status.HTTP_404_NOT_FOUND)
    
    instructor.delete()
    
    return Response({"message": "Instructor deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



#________________get instructor by department________________

@api_view(["GET"])
def get_instructors_by_department(request):
    department = request.query_params.get('department')
    
    if not department:
        return Response({"error": "Department query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    instructors = Instructor.objects.filter(department__iexact=department)
    
    if not instructors.exists():
        return Response({"error": "No instructors found for this department"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = InstructorSerializer(instructors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



