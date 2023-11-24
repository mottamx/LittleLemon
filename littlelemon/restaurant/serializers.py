from rest_framework import serializers
from .models import Menu, Booking
from django.contrib.auth.models import User

class MenuSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Menu
		fields = ['id','title','price','inventory']

class BookingSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Booking
		fields = '__all__'
  
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True, 'style': {'input_type': 'password'}}}
