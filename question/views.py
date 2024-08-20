from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Question
from .serializers import QuestionSerializer



@api_view(["POST"])
def create_question(request):
    serializer = QuestionSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def get_question_by_id(request):
    question_id = request.query_params.get('id')
    
    if not question_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    question = Question.objects.filter(pk=question_id).first()
    
    if not question:
        return Response({"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = QuestionSerializer(question)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_all_questions(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
def update_question(request):
    question_id = request.query_params.get('id')
    
    if not question_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    question = Question.objects.filter(pk=question_id).first()
    
    if not question:
        return Response({"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = QuestionSerializer(question, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_question(request):
    question_id = request.query_params.get('id')
    
    if not question_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    question = Question.objects.filter(pk=question_id).first()
    
    if not question:
        return Response({"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND)
    
    question.delete()
    return Response({"message": "Question deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def get_questions_by_quiz(request):
    quiz_id = request.query_params.get('quiz_id')
    
    if not quiz_id:
        return Response({"error": "Quiz ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    questions = Question.objects.filter(quiz=quiz_id)
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_questions_by_type(request):
    question_type = request.query_params.get('type')
    
    if not question_type:
        return Response({"error": "Question Type query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    questions = Question.objects.filter(question_type=question_type)
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
