from rest_framework import serializers
from blog.models import Tag
from .post import PostDetailSerializer

class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TagDetailSerializer(serializers.ModelSerializer):
    posts = PostDetailSerializer(many=True)
    class Meta:
        model = Tag
        fields = ('name','posts')


class TagCreateSerializer(serializers.ModelSerializer):
    

    def create(self, validated_data):
        tag = Tag(**validated_data)
        tag.save()
        return tag
    
    class Meta:
        model = Tag
        exclude = ('id','posts')
