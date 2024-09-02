from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import StudentScore, StudentAnswer
from .serializers import StudentScoreSerializer, StudentAnswerSerializer

# Create a new student score
@api_view(['POST'])
def create_student_score(request):
    serializer = StudentScoreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get a student score by ID
@api_view(['GET'])
def get_student_score_by_id(request):
    student_score_id = request.query_params.get('id')
    
    if not student_score_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    student_score = StudentScore.objects.filter(id=student_score_id).first()
    if student_score is None:
        raise NotFound(detail="StudentScore not found")

    serializer = StudentScoreSerializer(student_score)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Get all student scores
@api_view(['GET'])
def get_all_student_scores(request):
    student_scores = StudentScore.objects.all()
    serializer = StudentScoreSerializer(student_scores, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Update a student score
@api_view(['PUT'])
def update_student_score(request):
    student_score_id = request.query_params.get('id')
    
    if not student_score_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    student_score = StudentScore.objects.filter(id=student_score_id).first()
    if student_score is None:
        raise NotFound(detail="StudentScore not found")

    serializer = StudentScoreSerializer(student_score, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete a student score
@api_view(['DELETE'])
def delete_student_score(request):
    student_score_id = request.query_params.get('id')
    
    if not student_score_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    student_score = StudentScore.objects.filter(id=student_score_id).first()
    if student_score is None:
        raise NotFound(detail="StudentScore not found")

    student_score.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def get_scores_by_student(request):
    student_id = request.query_params.get('student_id')
    
    if not student_id:
        return Response({"error": "student_id query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    student_scores = StudentScore.objects.filter(student_id=student_id)
    
    serializer = StudentScoreSerializer(student_scores, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_scores_by_quiz(request):
    quiz_id = request.query_params.get('quiz_id')
    
    if not quiz_id:
        return Response({"error": "quiz_id query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    quiz_scores = StudentScore.objects.filter(quiz_id=quiz_id)
    serializer = StudentScoreSerializer(quiz_scores, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)




##################### student answer#####################



@api_view(['POST'])
def create_student_answer(request):
    serializer = StudentAnswerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get a student answer by ID
@api_view(['GET'])
def get_student_answer_by_id(request):
    student_answer_id = request.query_params.get('id')
    
    if not student_answer_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    student_answer = StudentAnswer.objects.filter(id=student_answer_id).first()
    if student_answer is None:
        raise NotFound(detail="StudentAnswer not found")

    serializer = StudentAnswerSerializer(student_answer)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Get all student answers
@api_view(['GET'])
def get_all_student_answers(request):
    student_answers = StudentAnswer.objects.all()
    serializer = StudentAnswerSerializer(student_answers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Update a student answer
@api_view(['PUT'])
def update_student_answer(request):
    student_answer_id = request.query_params.get('id')
    
    if not student_answer_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    student_answer = StudentAnswer.objects.filter(id=student_answer_id).first()
    if student_answer is None:
        raise NotFound(detail="StudentAnswer not found")

    serializer = StudentAnswerSerializer(student_answer, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete a student answer
@api_view(['DELETE'])
def delete_student_answer(request):
    student_answer_id = request.query_params.get('id')
    
    if not student_answer_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    student_answer = StudentAnswer.objects.filter(id=student_answer_id).first()
    if student_answer is None:
        raise NotFound(detail="StudentAnswer not found")

    student_answer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# views.py
@api_view(['GET'])
def get_answers_by_student(request):
    student_id = request.query_params.get('student_id')
    
    if not student_id:
        return Response({"error": "student_id query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    student_answers = StudentAnswer.objects.filter(student_id=student_id)
    serializer = StudentAnswerSerializer(student_answers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def get_answers_by_quiz(request):
    quiz_id = request.query_params.get('quiz_id')
    
    if not quiz_id:
        return Response({"error": "quiz_id query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    quiz_answers = StudentAnswer.objects.filter(question__quiz_id=quiz_id)
    serializer = StudentAnswerSerializer(quiz_answers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)




@api_view(['GET'])
def get_student_answers_summary(request):
    student_id = request.query_params.get('student_id')
    
    if not student_id:
        return Response({"error": "student_id query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    student_answers = StudentAnswer.objects.filter(student_id=student_id)
    correct_count = student_answers.filter(answer__is_correct=True).count()
    incorrect_count = student_answers.filter(answer__is_correct=False).count()
    
    summary = {
        'correct_answers': correct_count,
        'incorrect_answers': incorrect_count,
        'total_answers': student_answers.count()
    }
    
    return Response(summary, status=status.HTTP_200_OK)
