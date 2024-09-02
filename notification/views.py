from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Notification
from .serializer import NotificationSerializer
from uuid import UUID
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


#___________________create notification_________________

def send_notification_to_student(student_id, notification_id, message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'student_{student_id}',
        {
            'type': 'notification_message',
            'id': notification_id,
            'message': message
        }
    )

@api_view(["POST"])
def create_notification(request):
    data = request.data
    serializer = NotificationSerializer(data=data)
    
    if serializer.is_valid():
        notification = serializer.save()
        
        # Send notification to WebSocket channel
        student_id = notification.recipient.id
        notification_id = str(notification.id)  
        message = notification.message
        send_notification_to_student(student_id, notification_id, message)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
