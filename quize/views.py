from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Quiz
from .serializer import QuizSerializer

@api_view(["POST"])
def create_quiz(request):
    serializer = QuizSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def get_quiz_by_id(request):
    quiz_id = request.query_params.get('id')
    
    if not quiz_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    quiz = Quiz.objects.filter(pk=quiz_id).first()
    
    if not quiz:
        return Response({"error": "Quiz not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = QuizSerializer(quiz)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(["GET"])
def get_all_quizzes(request):
    quizzes = Quiz.objects.all()
    serializer = QuizSerializer(quizzes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(["PUT"])
def update_quiz(request):
    quiz_id = request.query_params.get('id')
    
    if not quiz_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    quiz = Quiz.objects.filter(pk=quiz_id).first()
    
    if not quiz:
        return Response({"error": "Quiz not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = QuizSerializer(quiz, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(["DELETE"])
def delete_quiz(request):
    quiz_id = request.query_params.get('id')
    
    if not quiz_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    quiz = Quiz.objects.filter(pk=quiz_id).first()
    
    if not quiz:
        return Response({"error": "Quiz not found"}, status=status.HTTP_404_NOT_FOUND)
    
    quiz.delete()
    return Response({"message": "Quiz deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



@api_view(["GET"])
def get_quizzes_by_module(request):
    module_id = request.query_params.get('module_id')
    
    if not module_id:
        return Response({"error": "Module ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    quizzes = Quiz.objects.filter(module=module_id)
    serializer = QuizSerializer(quizzes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_quizzes_by_instructor(request):
    instructor_id = request.query_params.get('instructor_id')
    
    if not instructor_id:
        return Response({"error": "Instructor ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    quizzes = Quiz.objects.filter(instructor=instructor_id)
    serializer = QuizSerializer(quizzes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
