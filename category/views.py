from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serialization import categoryserialization
from rest_framework.exceptions import NotFound


#______________create category ___________________

@api_view(["POST"])
def create_category(request):
    data = request.data
    serializer = categoryserialization(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#______________ get category by id ___________________

@api_view(["GET"])
def get_category_by_id(request, id):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        raise NotFound(detail="Category not found")
    
    serializer = categoryserialization(category)
    return Response(serializer.data, status=status.HTTP_200_OK)


#_______________ get all category _____________

@api_view(["GET"])
def get_all_categories(request):
    categories = Category.objects.all()
    serializer = categoryserialization(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


#______________update category _______________

@api_view(["PUT"])
def update_category(request, id):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response({"detail": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = categoryserialization(category, data=request.data, partial=True)  
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#________________ delete category ________________________

@api_view(["DELETE"])
def delete_category(request, id):
    try:
        category = Category.objects.get(pk=id)
        category.delete()
        return Response({"detail": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Category.DoesNotExist:
        return Response({"detail": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
    
    

#______________ get category by status _____________
 
@api_view(["GET"])
def get_categories_by_status(request):
    is_active = request.query_params.get('is_active', None)
    if is_active is not None:
        is_active = is_active.lower() in ['true', '1', 'yes']
        categories = Category.objects.filter(is_active=is_active)
    else:
        categories = Category.objects.all()
    
    serializer = categoryserialization(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)