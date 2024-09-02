from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Answer
from .serializers import AnswerSerializer
import uuid

@api_view(["POST"])
def create_answer(request):
    serializer = AnswerSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_answer_by_id(request):
    answer_id = request.query_params.get('id')
    
    if not answer_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        answer = Answer.objects.get(pk=uuid.UUID(answer_id))
    except Answer.DoesNotExist:
        return Response({"error": "Answer not found"}, status=status.HTTP_404_NOT_FOUND)
    except ValueError:
        return Response({"error": "Invalid ID format"}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = AnswerSerializer(answer)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_all_answers(request):
    answers = Answer.objects.all()
    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["PUT"])
def update_answer(request):
    answer_id = request.query_params.get('id')
    
    if not answer_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        answer = Answer.objects.get(pk=uuid.UUID(answer_id))
    except Answer.DoesNotExist:
        return Response({"error": "Answer not found"}, status=status.HTTP_404_NOT_FOUND)
    except ValueError:
        return Response({"error": "Invalid ID format"}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = AnswerSerializer(answer, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_answer(request):
    answer_id = request.query_params.get('id')
    
    if not answer_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        answer = Answer.objects.get(pk=uuid.UUID(answer_id))
    except Answer.DoesNotExist:
        return Response({"error": "Answer not found"}, status=status.HTTP_404_NOT_FOUND)
    except ValueError:
        return Response({"error": "Invalid ID format"}, status=status.HTTP_400_BAD_REQUEST)
    
    answer.delete()
    return Response({"message": "Answer deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
def get_answers_by_question(request):
    question_id = request.query_params.get('question_id')
    
    if not question_id:
        return Response({"error": "Question ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        answers = Answer.objects.filter(question=uuid.UUID(question_id))
    except ValueError:
        return Response({"error": "Invalid Question ID format"}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_answers_by_correctness(request):
    is_correct = request.query_params.get('is_correct')

    if is_correct is None:
        return Response({"error": "Correctness query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    if is_correct.lower() not in ['true', 'false']:
        return Response({"error": "Invalid value for correctness. Use 'true' or 'false'"}, status=status.HTTP_400_BAD_REQUEST)
    
    is_correct = is_correct.lower() == 'true'
    
    answers = Answer.objects.filter(is_correct=is_correct)
    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)












