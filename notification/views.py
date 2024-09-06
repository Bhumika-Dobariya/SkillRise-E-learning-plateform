from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .utils import send_sms
from .models import Notification
from uuid import UUID
from .serializer import NotificationSerializer


@api_view(["POST"])
def send_notification(request):
    phone_number = request.data.get('phone_number')
    message_body = request.data.get('message')
    notification_type = request.data.get('notification_type')
    
    if not phone_number or not message_body or not notification_type:
        return Response({"error": "Phone number, message, and notification type are required"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Create and save the notification in the database
    notification = Notification(
        recipient=None,  # Update this if you have a recipient model or logic
        message=message_body,
        notification_type=notification_type,
        phone_number=phone_number
    )
    notification.save()
    
    try:
        message_sid = send_sms(phone_number, message_body)
        
        return Response({
            "message": "Notification sent successfully",
            "message_sid": message_sid,
            "notification_type": notification_type
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        notification.delete()
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


#_________________get notification by id ________________

@api_view(["GET"])
def get_notification_by_id(request):
    id = request.query_params.get('id')
    
    if not id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        id = UUID(id)
    except ValueError:
        return Response({"error": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)
    
    notification = Notification.objects.filter(pk=id).first()
    
    if not notification:
        return Response({"error": "Notification not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = NotificationSerializer(notification)
    return Response(serializer.data, status=status.HTTP_200_OK)


#___________get all notifications_________________

@api_view(["GET"])
def get_all_notifications(request):
    notifications = Notification.objects.filter(is_deleted=False)
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


#______________update notification______________

@api_view(["PUT"])
def update_notification(request):
    id = request.query_params.get('id')
    
    if not id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        id = UUID(id)
    except ValueError:
        return Response({"error": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)
    
    notification = Notification.objects.filter(pk=id).first()
    
    if not notification:
        return Response({"error": "Notification not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = NotificationSerializer(notification, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#______________delete notification _________________

@api_view(["DELETE"])
def delete_notification(request):
    id = request.query_params.get('id')
    
    if not id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        id = UUID(id)
    except ValueError:
        return Response({"error": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)
    
    notification = Notification.objects.filter(pk=id).first()
    
    if not notification:
        return Response({"error": "Notification not found"}, status=status.HTTP_404_NOT_FOUND)
    
    notification.delete() 
    
    return Response({"message": "Notification deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



#______________mark notification as read_________________

@api_view(["POST"])
def mark_notification_as_read(request):
    id = request.query_params.get('id')
    
    if not id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        id = UUID(id)
    except ValueError:
        return Response({"error": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)
    
    notification = Notification.objects.filter(pk=id).first()
    
    if not notification:
        return Response({"error": "Notification not found"}, status=status.HTTP_404_NOT_FOUND)
    
    notification.is_read = True
    notification.save()
    
    return Response({"message": "Notification marked as read"}, status=status.HTTP_200_OK)
