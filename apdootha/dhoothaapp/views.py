from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from dhoothaapp.models import Account
from dhoothaapp.serializer import AccountSerializer,AccountSerializer1
from django.forms.models import model_to_dict
from rest_framework import status
import json
from django.contrib.auth import authenticate,get_user_model
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            if user.is_staff:
                role="admin"
            else:
                role="member"
            if user.phone is not None:
                phone=user.phone
            else:
                phone="9501834834"
            return Response({'token': token.key,'username':user.username,"email":user.email,"phone":phone,"role":role}, status=status.HTTP_200_OK)
        else:
            return Response({'username': 'Invalid Credentials',"password":"wrong"}, status=status.HTTP_401_UNAUTHORIZED)
class Registration(APIView):
    def post(self, request):
        username = request.data.get('username')
        User = get_user_model()

        users = Account.objects.get(username=username)
        dic={"username":users.username,"name":users.first_name+" "+users.last_name,"email":users.email,
             "phone":users.phone,"pincode":users.pincode,"village":users.village,"madal":users.mandal
             ,"doj":users.doj,"dor":users.dor,"photo":str(users.profile_image)}
        return Response(dic)
    def put(self, request, *args, **kwargs):
        d=request.data
        cuser=d["username"]
        ro=Account.objects.get(username=cuser)
        ro.email=d["email"]
        ro.pincode=d["pincode"]
        ro.village=d["village"]
        ro.mandal=d["mandal"]
        ro.profile_image=d["photo"]
        ro.save()
        return Response({"message":f"{cuser} profile update successfully"})
class AddMember(APIView):
    def post(self,request):
        data=request.data
        data["password"]=make_password(data["password"])
        serializer = AccountSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)