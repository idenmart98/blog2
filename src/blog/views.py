import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .models import Post, Tag
from .serializers import (
    PostListSerializer, 
    PostDetailSerializer, 
    TagListSerializer, 
    TagDetailSerializer,
    PostCreateSerializer,
    TagCreateSerializer
    )
from .forms import TagCreateForm, PostCreateForm


class PostListView(ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()

class PostDetailView(RetrieveAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    lookup_field = 'pk'
    lookup_url_kwarg = 'post_id'

class TagListView(ListAPIView):
    serializer_class = TagListSerializer
    queryset = Tag.objects.all()


class TagDetailView(RetrieveAPIView):
    serializer_class = TagDetailSerializer
    queryset = Tag.objects.all()
    lookup_field = 'pk'
    lookup_url_kwarg = 'tag_id'


class PostCreateView(CreateAPIView):
    serializer_class = PostCreateSerializer

class TagCreateView(CreateAPIView):
    serializer_class = TagCreateSerializer 

def post_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request,'list_post.html',{'posts':posts})


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request,'post_detail.html',{'post':post})

def tag_detail(request, tag_id):
    posts = Post.objects.filter(tags__id = tag_id)
    return render(request,'list_post.html',{'posts':posts})

def tag_list(request):
    tags = Tag.objects.all().order_by('-id')
    return render(request,'tag_list.html',{'tags':tags})

def tag_create(request):
    form = TagCreateForm()
    if request.method == "POST":
        save_form = TagCreateForm(request.POST)
        if save_form.is_valid():
            save_form.save()
            return redirect('blog:tag_list')
    return render(request,'tag_create.html',{'form':form})

def post_create(request):
    form = PostCreateForm()
    if request.method == "POST":
        save_form = PostCreateForm(request.POST)
        if save_form.is_valid():
            save_form.save()
            return redirect('blog:post_list')
    return render(request,'tag_create.html',{'form':form})