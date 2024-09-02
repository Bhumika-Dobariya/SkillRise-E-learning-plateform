from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Subscription
from .serializers import SubscriptionSerializer

@api_view(["POST"])
def create_subscription(request):
    serializer = SubscriptionSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_subscription_by_id(request):
    subscription_id = request.query_params.get('id')
    
    if not subscription_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    subscription = Subscription.objects.filter(pk=subscription_id).first()
    
    if not subscription:
        return Response({"error": "Subscription not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = SubscriptionSerializer(subscription)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_all_subscriptions(request):
    subscriptions = Subscription.objects.all()
    serializer = SubscriptionSerializer(subscriptions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["PUT"])
def update_subscription(request):
    subscription_id = request.query_params.get('id')
    
    if not subscription_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    subscription = Subscription.objects.filter(pk=subscription_id).first()
    
    if not subscription:
        return Response({"error": "Subscription not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = SubscriptionSerializer(subscription, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_subscription(request):
    subscription_id = request.query_params.get('id')
    
    if not subscription_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    subscription = Subscription.objects.filter(pk=subscription_id).first()
    
    if not subscription:
        return Response({"error": "Subscription not found"}, status=status.HTTP_404_NOT_FOUND)
    
    subscription.delete()
    return Response({"message": "Subscription deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
def get_subscriptions_by_student(request):
    student_id = request.query_params.get('student_id')
    
    if not student_id:
        return Response({"error": "Student ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    subscriptions = Subscription.objects.filter(student=student_id)
    serializer = SubscriptionSerializer(subscriptions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

