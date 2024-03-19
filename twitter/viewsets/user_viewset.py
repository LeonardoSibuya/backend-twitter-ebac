from rest_framework import viewsets
from twitter.models import User
from twitter.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer