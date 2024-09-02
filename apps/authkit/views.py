from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import exceptions

# Create your views here.
class RegisterView(APIView):
    def post(self,request):
        
        
        data = request.data
        
        if data.get('password') != data.get('password_confirm'):
            raise exceptions.APIException('password do not match')
    
        serializers = UserSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
