from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Super
from .serializers import SuperSerializer

@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        s_type = request.query_params.get('type')
        s_name = request.query_params.get('name')


        queryset = Super.objects.all()

        if s_type:
            queryset = queryset.filter(super_type__type= s_type)
        if s_name:
            queryset = queryset.filter(name=s_name)    

        serializer = SuperSerializer(queryset, many=True)    
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super);
        return Response(serializer.data)
    elif request.method == 'PUT':
         serializer = SuperSerializer(super, data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 