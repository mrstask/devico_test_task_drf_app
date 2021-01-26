from rest_framework import serializers

from social.models import Post, PostLike


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title',
                  'description',
                  'text',
                  'id'
                  )

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        post = Post(**validated_data)
        post.save()
        return post


class PostLikeSerializer(serializers.ModelSerializer):
    is_like = serializers.BooleanField(required=False)

    class Meta:
        model = Post
        fields = ('is_like', )

    def update(self, instance, validated_data):
        if validated_data['is_like']:
            instance.like.add(self.context['request'].user)
        else:
            if self.context['request'].user in instance.like.all():
                instance.like.remove(self.context['request'].user)
        return instance


class PostAnalyticsSerializer(serializers.ModelSerializer):
    likes = serializers.IntegerField()

    class Meta:
        model = PostLike
        fields = ('like_date', 'likes')






