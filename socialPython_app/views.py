from django.shortcuts import render
from socialPython_app.models import userModel
from socialPython_app.serializers import userSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


# from django.http import JsonResponse
# Create your views here.

class user_list(generics.ListCreateAPIView):
    queryset= userModel.objects.all()
    serializer_class= userSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

class user_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset= userModel.objects.all()
    serializer_class= userSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]



"""
@api_view(['GET', 'POST'])
def user_list(request):

    if request.method == 'GET':
        users = userModel.objects.all()
        serializer = userSerializer(users, many=True)        
        return Response(serializer.data)
        authentication_classes=[BasicAuthentication]
        permission_classes=[IsAuthenticated]

    elif request.method == 'POST':
        serializer = userSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.error.HTTP_400_BAD_REQUEST)
        


def employeeView(request):
    emp={
        'id':123,
        'name':'atul',
        'sal': 100000
    }
    return JsonResponse(emp)
"""