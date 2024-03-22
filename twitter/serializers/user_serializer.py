from rest_framework import serializers
from twitter.serializers.tweet_serializer import TweetSerializer

from twitter.models import User

class UserSerializer(serializers.ModelSerializer):
    follows = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()
    tweets = TweetSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'follows', 'followers', 'tweets']
        
    def get_follows(self, obj):
        return obj.follows.values('id', 'name', 'email', 'follows', 'followers', 'tweet')
    
    def get_followers(self, obj):
        return obj.followers.values('id', 'name', 'email', 'follows', 'followers', 'tweet')
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        tweets = instance.get_tweets()  # Obtenha os tweets do usuário
        tweet_serializer = TweetSerializer(tweets, many=True)  # Serialize os tweets
        data['tweets'] = tweet_serializer.data  # Adicione os tweets serializados aos dados
        return data