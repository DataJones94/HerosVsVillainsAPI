from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SuperType
from .serializers import SuperTypeSerializer

@api_view(['GET', 'POST'])
def super_types_list(request):
    if request.method == 'GET':
        # dealership_name = request.query_params.get('dealership')
        # print(dealership_name)

        queryset = SuperType.objects.all()

        # if dealership_name:
        #     queryset = queryset.filter(dealership__name= dealership_name)

        serializer = SuperTypeSerializer(queryset, many=True)    
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = SuperTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)