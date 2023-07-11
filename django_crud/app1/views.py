from django.shortcuts import render
from .Serializers import EmployeeSerializer
from rest_framework.views import APIView
from .models import Employee
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.generics import UpdateAPIView
from rest_framework import viewsets



class EmployeeView(APIView):

    def get(self,request):
        obj = Employee.objects.all()
        serializers = EmployeeSerializer(obj, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)
    

    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view()
def get_v(request, pk):
    obj = get_object_or_404(Employee ,pk=pk)
    serializer = EmployeeSerializer(obj)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
    

class Update_v(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class Partial_v(viewsets.ViewSet):

    def partial_update(self, request, pk):
        obj = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(data=request.data, instance=obj, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def destroy(self, request, pk):
        obj = get_object_or_404(Employee, pk=pk)
        obj.delete()
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)