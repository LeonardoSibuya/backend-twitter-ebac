from django.contrib import admin
from django.urls import include, path
from twitter.viewsets import UserViewSet, TweetCreateViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'users/signup', UserViewSet, basename='signup')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
    path('users/<int:user_id>/tweet/', TweetCreateViewSet.as_view({'post': 'create'}), name='user_tweet_create'),
    path('users/tweet/<int:tweet_id>/delete/', TweetCreateViewSet.as_view({'delete': 'delete_tweet'}), name='tweet-delete'),

    # path('api-auth/', include('rest_framework.urls')),
    # path('api-token-auth/', obtain_auth_token, name='api-token-auth')
]
