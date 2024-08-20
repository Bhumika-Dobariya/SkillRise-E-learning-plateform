from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer

@api_view(["POST"])
def create_payment(request):
    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_payment_by_id(request):
    payment_id = request.query_params.get('id')
    if not payment_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        payment = Payment.objects.get(pk=payment_id)
    except Payment.DoesNotExist:
        return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = PaymentSerializer(payment)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_all_payments(request):
    payments = Payment.objects.all()
    serializer = PaymentSerializer(payments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["PUT"])
def update_payment(request):
    payment_id = request.query_params.get('id')
    if not payment_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        payment = Payment.objects.get(pk=payment_id)
    except Payment.DoesNotExist:
        return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = PaymentSerializer(payment, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_payment(request):
    payment_id = request.query_params.get('id')
    if not payment_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        payment = Payment.objects.get(pk=payment_id)
    except Payment.DoesNotExist:
        return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)
    payment.delete()
    return Response({"message": "Payment deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
