from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Module
from .serializer import ModuleSerializer




@api_view(["POST"])
def create_module(request):
    data = request.data
    serializer = ModuleSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(["GET"])
def get_module_by_id(request):
    module_id = request.query_params.get('id')
    
    if not module_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    module = Module.objects.filter(pk=module_id).first()
    
    if not module:
        return Response({"error": "Module not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ModuleSerializer(module)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(["GET"])
def get_all_modules(request):
    modules = Module.objects.all()
    serializer = ModuleSerializer(modules, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(["PUT"])
def update_module(request):
    module_id = request.query_params.get('id')
    
    if not module_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    module = Module.objects.filter(pk=module_id).first()
    
    if not module:
        return Response({"error": "Module not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ModuleSerializer(module, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(["DELETE"])
def delete_module(request):
    module_id = request.query_params.get('id')
    
    if not module_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    module = Module.objects.filter(pk=module_id).first()
    
    if not module:
        return Response({"error": "Module not found"}, status=status.HTTP_404_NOT_FOUND)
    
    module.delete()
    
    return Response({"message": "Module deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



@api_view(["GET"])
def get_modules_by_course(request):
    course_id = request.query_params.get('course_id')
    
    if not course_id:
        return Response({"error": "Course ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    modules = Module.objects.filter(course_id=course_id)
    serializer = ModuleSerializer(modules, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_published_modules(request):
    modules = Module.objects.filter(is_published=True)
    serializer = ModuleSerializer(modules, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_unpublished_modules(request):
    modules = Module.objects.filter(is_published=False)
    serializer = ModuleSerializer(modules, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PATCH"])
def publish_module(request):
    module_id = request.query_params.get('id')
    
    if not module_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    module = Module.objects.filter(pk=module_id).first()
    
    if not module:
        return Response({"error": "Module not found"}, status=status.HTTP_404_NOT_FOUND)
    
    module.is_published = True
    module.save()
    
    serializer = ModuleSerializer(module)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PATCH"])
def unpublish_module(request):
    module_id = request.query_params.get('id')
    
    if not module_id:
        return Response({"error": "ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    module = Module.objects.filter(pk=module_id).first()
    
    if not module:
        return Response({"error": "Module not found"}, status=status.HTTP_404_NOT_FOUND)
    
    module.is_published = False
    module.save()
    
    serializer = ModuleSerializer(module)
    return Response(serializer.data, status=status.HTTP_200_OK)