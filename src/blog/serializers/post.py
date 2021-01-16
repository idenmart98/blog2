from rest_framework import serializers
from blog.models import Post

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('body','tags')

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('id',)

class PostCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        post = Post(**validated_data)
        post.save()
        return post
    
    class Meta:
        model = Post
        exclude = ('id',)
