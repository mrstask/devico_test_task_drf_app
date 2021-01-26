from django.db.models import Count

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from social.models import Post, PostLike
from social.serializers import PostListSerializer, PostLikeSerializer, PostAnalyticsSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]


class PostDetails(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostLikeSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class PostAnalytics(generics.ListAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostAnalyticsSerializer
    filter_backends = [DjangoFilterBackend, ]

    filterset_fields = {
        'like_date': ['gte', 'lte', 'exact', 'gt', 'lt']
    }

    def get_queryset(self):
        return PostLike.objects.all().values('like_date').annotate(likes=Count('post'))



