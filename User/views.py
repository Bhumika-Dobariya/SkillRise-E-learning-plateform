from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import User,BlacklistedToken
from .serialization import UserSerializer
from rest_framework.exceptions import NotFound
from django.core.mail import send_mail
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, OTP
from .serialization import OTPRequestSerializer, OTPVerificationRequestSerializer
import random
import uuid
from datetime import timedelta
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from .utils.token import get_token,decode_token_user_id
import bcrypt
from django.conf import settings
from django.contrib.auth.hashers import make_password
from jose import JWTError
from .permission import IsAdmin, IsInstructor, IsStudent
from django.core.exceptions import ValidationError
from rest_framework.exceptions import AuthenticationFailed


@api_view(['GET'])
@permission_classes([IsAdmin])
def admin_only_view(request):
    return Response({"message": "Welcome, Admin!"}, status=status.HTTP_200_OK)



#_____________________ create user ________________________

@api_view(["POST"])
def create_user(request):
    data = request.data
    data["password"] = bcrypt.hashpw(
        data["password"].encode("utf-8"), bcrypt.gensalt()
    ).decode("utf-8")
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#_______________ generate otp _____________________

@api_view(['POST'])
def generate_otp(request):
    serializer = OTPRequestSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        user = User.objects.filter(email=email).first() 

        if not user:
            return Response({'error': 'Invalid or missing email address'}, status=status.HTTP_400_BAD_REQUEST)

        OTP.objects.filter(user_email=email, is_active=True).update(is_active=False, is_deleted=True)

        otp_code = str(random.randint(100000, 999999))
        expiration_time = timezone.now() + timedelta(minutes=10)

        OTP.objects.create(
            id=uuid.uuid4(),
            user_email=email,
            otp=otp_code,
            expiration_time=expiration_time
        )

        send_otp_email(email, otp_code)
        return Response({"message": "OTP generated and sent successfully to the provided email address."})

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# send_otp_email

def send_otp_email(email, otp_code):
    subject = "Your OTP Code"
    message = f"Your OTP is {otp_code} which is valid for 10 minutes"
    from_email = 'bhumikadobariya2412@gmail.com'  
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
   
   
    
#___________________ verify_otp __________________

@api_view(['POST'])
def verify_otp(request):
    serializer = OTPVerificationRequestSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        entered_otp = serializer.validated_data['otp']

        otps = OTP.objects.filter(user_email=email, is_active=True)

        if otps.exists():
            for stored_otp in otps:
                if timezone.now() < stored_otp.expiration_time:
                    if entered_otp == stored_otp.otp:
                        stored_otp.is_active = False
                        stored_otp.is_deleted = True
                        stored_otp.save()

                        user = User.objects.filter(email=email, is_active=True, is_deleted=False).first()
                        if user:
                            user.is_verified = True
                            user.save()
                            return Response({"message": "OTP verification successful"})

                        return Response({"error": "User is not verified"}, status=status.HTTP_400_BAD_REQUEST)

                    return Response({"error": "Incorrect OTP entered"}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    stored_otp.delete()

            return Response({"error": "OTP has expired"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"error": "No OTP found"}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#___________________logging___________________



@api_view(["POST"])
def login_or_register(request):
    uname = request.data.get("uname")
    password = request.data.get("password")
    
    if not uname or not password:
        return Response({"message": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
      
        user = User.objects.get(name=uname)
    except User.DoesNotExist:
        try:
            user = User.objects.get(email=uname)
        except User.DoesNotExist:
            
            hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode('utf-8')
            user = User.objects.create(name=uname, email=uname, password=hashed_password)
      
            token = get_token(user)
            role = user.role
            return Response({
                "message": "User registered and logged in successfully",
                "token": token,
                "role": role
            }, status=status.HTTP_201_CREATED)
 
    if bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
        if not user.is_active:
            return Response({"message": "User account is inactive"}, status=status.HTTP_403_FORBIDDEN)
        token = get_token(user)
        role = user.role
        
        return Response({
            "token": token,
            "role": role  
        }, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

    
    


@api_view(['GET'])
@permission_classes([IsInstructor])
def instructor_only_view(request):
    return Response({"message": "Welcome, Instructor!"}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsStudent])
def student_only_view(request):
    return Response({"message": "Welcome, Student!"}, status=status.HTTP_200_OK)  



#_______________ get_user_by_id __________________

@api_view(["GET"])
@permission_classes([IsAdmin])
def get_user_by_id(request, id):
    try:
        user = User.objects.get(pk=id, is_active=True, is_deleted=False)
    except User.DoesNotExist:
        raise NotFound(detail="User not found")
    
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


#__________________ get_user_by_token ________________

@api_view(['GET'])
@permission_classes([IsAdmin])
def get_user_by_token(request):
    token = request.headers.get('Authorization')
    if not token:
        return Response({"error": "Token is required"}, status=status.HTTP_400_BAD_REQUEST)

    user_id = decode_token_user_id(token)
    if not user_id:
        return Response({"error": "Invalid token or user ID extraction failed"}, status=status.HTTP_400_BAD_REQUEST)

 
    db_user = User.objects.filter(id=user_id, is_active=True, is_verified=True, is_deleted=False).first()
    if db_user is None:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(db_user)
    return Response(serializer.data)


#_______________ get all user __________________

@api_view(["GET"])
@permission_classes([IsAdmin])
def get_all_user(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


#______________ update user by id ___________________

@api_view(['PUT'])
@permission_classes([IsAdmin])
def update_user(request, id):
    try:
        user = User.objects.get(pk=id, is_active=True, is_deleted=False)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = UserSerializer(user, data=request.data, partial=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#__________________ update_user_by_token ___________________

@api_view(['PUT'])
@permission_classes([IsAdmin])
def update_user_by_token(request):
    token = request.headers.get('Authorization')
    
    if not token:
        return Response({'error': 'Token is missing'}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        user_id_from_token = decode_token_user_id(token)
    except JWTError:
        return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        user = User.objects.get(pk=user_id_from_token, is_active=True, is_verified=True, is_deleted=False)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if user_id_from_token != str(user.id):
        return Response({'error': 'Unauthorized to update this user'}, status=status.HTTP_403_FORBIDDEN)
    
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#____________delete user by id _________________

@api_view(['DELETE'])
@permission_classes([IsAdmin])
def user_delete(request, id):
    try:
        user = User.objects.get(pk=id, is_active=True, is_deleted=False)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    user.is_deleted = True
    user.save()
    return Response({'message': 'User marked as deleted successfully'}, status=status.HTTP_204_NO_CONTENT)



#___________________ delete user by token_____________________

@api_view(['DELETE'])
@permission_classes([IsAdmin])
def user_delete_by_token(request):
    token = request.headers.get('Authorization')
    
    if not token:
        return Response({'error': 'Token is missing'}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        user_id_from_token = decode_token_user_id(token)
    except JWTError:
        return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        user_to_delete = User.objects.get(pk=user_id_from_token, is_active=True, is_verified=True, is_deleted=False)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if user_id_from_token != str(user_to_delete.id):
        return Response({'error': 'Unauthorized to delete this user'}, status=status.HTTP_403_FORBIDDEN)
    
    user_to_delete.is_deleted = True
    user_to_delete.save()
    return Response({'message': 'User marked as deleted successfully'}, status=status.HTTP_204_NO_CONTENT)



#__________________forget password by token____________________

@api_view(['PUT'])
def forget_password(request):
    token = request.headers.get('Authorization')
    new_password = request.data.get('user_newpass')

    if not token:
        return Response({'error': 'Token is missing'}, status=status.HTTP_401_UNAUTHORIZED)

    if not new_password:
        return Response({'error': 'New password is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user_id = decode_token_user_id(token)
    except JWTError:
        return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        db_user = User.objects.get(id=user_id, is_active=True, is_verified=True, is_deleted=False)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    if not db_user.is_verified:
        return Response({'error': 'User not verified'}, status=status.HTTP_403_FORBIDDEN)

    hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    db_user.password = hashed_password
    db_user.save()
    
    return Response({'message': 'Password reset successfully'}, status=status.HTTP_200_OK)



#___________________reset password by token____________________

@api_view(['PUT'])
def reset_password_by_token(request):
    token = request.headers.get('Authorization')
    old_password = request.data.get('old_password')
    new_password = request.data.get('new_password')

    if not token:
        return Response({'error': 'Token is missing'}, status=status.HTTP_401_UNAUTHORIZED)

    if not old_password or not new_password:
        return Response({'error': 'Old and new passwords are required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user_id = decode_token_user_id(token)
    except JWTError:
        return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        db_user = User.objects.get(id=user_id, is_active=True, is_verified=True, is_deleted=False)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    if not check_password(old_password, db_user.password):
        return Response({'error': 'Old password does not match'}, status=status.HTTP_400_BAD_REQUEST)

    db_user.password = make_password(new_password)
    db_user.save()

    return Response({'message': 'Password reset successfully'}, status=status.HTTP_200_OK)






@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        access_token = request.data.get('access_token')
        if not access_token:
            return Response({"error": "Access token is required"}, status=status.HTTP_400_BAD_REQUEST)

        if BlacklistedToken.objects.filter(token=access_token).exists():
            return Response({"message": "Token already blacklisted"}, status=status.HTTP_400_BAD_REQUEST)

        BlacklistedToken.objects.create(
            token=access_token,
            blacklisted_at=timezone.now()
        )

        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
