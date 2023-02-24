from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken


@api_view()
def hello_world(request):
    return Response({"status": 200, "message": "Hello, World!"})
# Create your views here.


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({"status": 403, "message": "Invalid req","error": serializer.errors})

        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        token_obj, _ = Token.objects.get_or_create(user = user)
        return Response({"status": 200, "data": serializer.data, "message": "Successful", "token": str(token_obj)})
    
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name
        })

class UserView(APIView):
    def get(self, request):
        authentication_classes = [TokenAuthentication]
        permission_classes = [IsAuthenticated]
        print(request.user)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"status": 200, "data": serializer.data, "message": "Successful"})

        