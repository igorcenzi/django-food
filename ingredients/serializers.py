from rest_framework import serializers

class IngredientSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=40)
  
  