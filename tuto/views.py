from django.shortcuts import render

# Create your views here.

from django.http.response import JsonResponse

from rest_framework.parsers import JSONParser 

from rest_framework import status
 
from tuto.models import Tuto

from tuto.serializers import TutoSerializer

from rest_framework.decorators import api_view






@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':

        tuto = Tuto.objects.all()
        
        title = request.GET.get('title', None)

        if title is not None:

            tuto = tuto.filter(title__icontains=title)
        
        tuto_serializer = TutoSerializer(tutorials, many=True)

        return JsonResponse(tuto_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':

        tuto_data = JSONParser().parse(request)

        tuto_serializer = TutoSerializer(data=tutorial_data)

        if tuto_serializer.is_valid():

            tuto_serializer.save()

            return JsonResponse(tuto_serializer.data, status=status.HTTP_201_CREATED) 

        return JsonResponse(tuto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        count = Tuto.objects.all().delete()

        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    # find tutorial by pk (id)
    try: 
        tuto = Tuto.objects.get(pk=pk) 
    except Tuto.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 

        tuto_serializer = TutoSerializer(tutorial) 

        return JsonResponse(tuto_serializer.data)

    elif request.method == 'PUT': 

        tuto_data = JSONParser().parse(request) 

        tuto_serializer = TutoSerializer(tuto, data=tuto_data) 

        if tuto_serializer.is_valid(): 

            tuto_serializer.save() 

            return JsonResponse(tuto_serializer.data) 

        return JsonResponse(tuto_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 

        tuto.delete() 

        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    # GET / PUT / DELETE tutorial
    
        
@api_view(['GET'])
def tutorial_list_published(request):
    # GET all published tutorials
    tuto = Tuto.objects.filter(published=True)
        
    if request.method == 'GET': 

        tuto_serializer = TutoSerializer(tuto, many=True)

        return JsonResponse(tuto_serializer.data, safe=False)