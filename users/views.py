from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from .models import User
from .serializers import UserSerializer
from users import serializers

# Create your views here.
class UserView(APIView):
  def get(self, request):    
      
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
  
  
  
  def post(self, request):
    
    serializer = UserSerializer(data=request.data)
    
    serializer.is_valid(raise_exception=True)
    
    serializer.save()
    
    return Response(serializer.data, status.HTTP_201_CREATED)
  
class UserViewDetail(APIView):
  def get(self, _ , user_id):    
    user = get_object_or_404(User, pk=user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data)
  
  def delete(self, request, user_id):
    user = get_object_or_404(User, pk=user_id)
    
    user.delete()
    
    return Response(status=status.HTTP_204_NO_CONTENT)
  
  def patch(self, request, user_id):
    user = get_object_or_404(User, pk=user_id)
    
    serializer = UserSerializer(user, request.data, partial=True)
    
    serializer.is_valid(raise_exception=True)
    try:
      
      serializer.save()
    except KeyError:
      return Response({'error': 'não pode atualizar endereço'}, status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.data, status.HTTP_200_OK)