from rest_framework import viewsets, status
from twitter.models import User
from twitter.serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=True, methods=['post'])
    def follow(self, request, pl=None):
        user = self.get_object()
        target_user_id = request.data.get('target_user_id')
        
        if target_user_id is None:
            return Response({"Error": "O ID do usúario é obrigatório"}, status=status.HTTP_400_BAD_REQUEST)
        
        target_user = User.objects.filter(pk=target_user_id).first()
        
        if target_user is None:
            return Response({"Error": "Usúario não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        # add follow and follower
        user.follows.add(target_user)
        target_user.followers.add(user)
        
        return Response({"Message:" "Você seguiu com sucesso o úsuario: ", target_user.name}, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['post'])
    def unfollow(self, request, pk=None):
        user = self.get_object()
        target_user_id = request.data.get('target_user_id')

        if target_user_id is None:
            return Response({"error": "O ID do usuário alvo é obrigatório"}, status=status.HTTP_400_BAD_REQUEST)

        target_user = User.objects.filter(pk=target_user_id).first()
        if target_user is None:
            return Response({"error": "Usuário alvo não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # remove follow and follower
        user.follows.remove(target_user)
        target_user.followers.remove(user)

        return Response({"message": "Você deixou de seguir com sucesso o usuário"}, status=status.HTTP_200_OK)