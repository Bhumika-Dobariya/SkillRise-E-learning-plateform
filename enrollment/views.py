from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Enrollment
from .serializer import EnrollmentSerializer




@api_view(["POST"])
def create_enrollment(request):
    serializer = EnrollmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def get_enrollment_by_id(request):
    id = request.query_params.get('id')
    
    if not id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    enrollment = Enrollment.objects.filter(pk=id).first()
    
    if not enrollment:
        return Response({"error": "Enrollment not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EnrollmentSerializer(enrollment)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_all_enrollments(request):
    enrollments = Enrollment.objects.all()
    serializer = EnrollmentSerializer(enrollments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)




@api_view(["PUT"])
def update_enrollment(request):
    id = request.query_params.get('id')
    
    if not id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    enrollment = Enrollment.objects.filter(pk=id).first()
    
    if not enrollment:
        return Response({"error": "Enrollment not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EnrollmentSerializer(enrollment, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(["DELETE"])
def delete_enrollment(request):
    id = request.query_params.get('id')
    
    if not id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    enrollment = Enrollment.objects.filter(pk=id).first()
    
    if not enrollment:
        return Response({"error": "Enrollment not found"}, status=status.HTTP_404_NOT_FOUND)
    
    enrollment.delete()
    return Response({"message": "Enrollment deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def get_enrollments_by_student(request):
    student_id = request.query_params.get('student_id')
    
    if not student_id:
        return Response({"error": "Student ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    enrollments = Enrollment.objects.filter(student_id=student_id)
    
    if not enrollments.exists():
        return Response({"message": "No enrollments found for this student"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EnrollmentSerializer(enrollments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)




@api_view(["GET"])
def get_enrollments_by_course(request):
    course_id = request.query_params.get('course_id')
    
    if not course_id:
        return Response({"error": "Course ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    enrollments = Enrollment.objects.filter(course_id=course_id)
    
    if not enrollments:
        return Response({"message": "No enrollments found for this course"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EnrollmentSerializer(enrollments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(["PATCH"])
def issue_certificate(request):
    id = request.query_params.get('id')
    
    if not id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    enrollment = Enrollment.objects.filter(pk=id).first()
    
    if not enrollment:
        return Response({"error": "Enrollment not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if enrollment.certificate_issued:
        return Response({"message": "Certificate already issued"}, status=status.HTTP_200_OK)
    
    enrollment.certificate_issued = True
    enrollment.save()
    
    return Response({"message": "Certificate issued successfully"}, status=status.HTTP_200_OK)





@api_view(["GET"])
def get_enrollments_by_completion_date(request):
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')
    
    if not start_date or not end_date:
        return Response({"error": "Start date and end date query parameters are required"}, status=status.HTTP_400_BAD_REQUEST)
    
    enrollments = Enrollment.objects.filter(completion_date__range=[start_date, end_date])
    
    if not enrollments:
        return Response({"message": "No enrollments found within this date range"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EnrollmentSerializer(enrollments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


