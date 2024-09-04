from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            token, created = Token.objects.get_or_create(user=user)
            if user.phone is not None:
                phone=user.phone
            else:
                phone="9501834834"
            return Response({'token': token.key,'username':user.username,"email":user.email,"phone":phone}, status=status.HTTP_200_OK)
        else:
            return Response({'username': 'Invalid Credentials',"password":"wrong"}, status=status.HTTP_401_UNAUTHORIZED)
