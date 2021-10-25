from django.shortcuts import render
from rest_framework.views import APIView
from .models import SchoolModel
from .serializers import SchoolSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class SchoolViewAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = SchoolModel.objects.get(id=id)
            serializer = SchoolSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        stu = SchoolModel.objects.all()
        serializer = SchoolSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = SchoolSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Record Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
