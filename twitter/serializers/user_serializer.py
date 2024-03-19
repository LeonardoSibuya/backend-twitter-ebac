from rest_framework import serializers
from twitter.serializers.tweet_serializer import TweetSerializer

from twitter.models import User

class UserSerializer(serializers.ModelSerializer):
    follows = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    followers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    tweets = TweetSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'follows', 'followers', 'tweets']
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        tweets = instance.get_tweets()  # Obtenha os tweets do usuário
        tweet_serializer = TweetSerializer(tweets, many=True)  # Serialize os tweets
        data['tweets'] = tweet_serializer.data  # Adicione os tweets serializados aos dados
        return data