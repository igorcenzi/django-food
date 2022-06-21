from rest_framework import serializers
from addresses.serializers import AddressSerializer
from users.models import User
from addresses.models import Address

class UserSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  first_name = serializers.CharField(max_length=10)
  last_name = serializers.CharField(max_length=10)
  email = serializers.EmailField(max_length=100)
  
  address = AddressSerializer()
  
  def create(self, validated_data: dict):
    address_data = validated_data.pop("address")
    user = User.objects.create(**validated_data)
    Address.objects.create(**address_data, user=user)
    
    return user
  
  def update(self, instance: User, validated_data: dict):
    
    non_editable_keys = ("address",)
  
    for key, value in validated_data.items():
      if key in non_editable_keys:
        raise KeyError
      setattr(instance, key, value)
      
    instance.save()
    
    return instance