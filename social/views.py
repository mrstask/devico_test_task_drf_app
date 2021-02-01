from django.db.models import Count

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from social.models import Post, PostLike
from social.serializers import PostListSerializer, PostLikeSerializer, PostAnalyticsSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]


class PostDetails(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = [IsAuthenticated]


class PostAnalytics(generics.ListAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostAnalyticsSerializer
    filter_backends = [DjangoFilterBackend, ]
    permission_classes = [IsAuthenticated]

    filterset_fields = {
        'like_date': ['gte', 'lte', 'exact', 'gt', 'lt']
    }

    def get_queryset(self):
        return PostLike.objects.all().values('like_date').annotate(likes=Count('post'))



