from dhoothaapp.models import Account
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account

        fields = ['username', 'first_name', 'last_name', 'phone','email','password','doj','dor']
        extra_kwargs = {'password': {'write_only': True}}
class AccountSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Account