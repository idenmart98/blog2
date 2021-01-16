from django.urls import path
from .views import (  
    PostCreateView,
    TagCreateView,
    PostListView,
    TagListView,
    PostDetailView,
    TagDetailView,
    post_list,
    post_detail,
    tag_detail,
    tag_list,
    post_create,
    tag_create)

app_name = 'blog'

urlpatterns = [
    path('api.posts/',PostListView.as_view()),
    path('api.post/<int:post_id>/',PostDetailView.as_view()),
    path('api.post/create/', PostCreateView.as_view()),
    path('api.tags/', TagListView.as_view()),
    path('api.tag/<int:tag_id>/', TagDetailView.as_view()),
    path('api.tag/create/', TagCreateView.as_view()),
    path('', post_list, name = 'post_list'),
    path('post/<int:post_id>/', post_detail, name = 'post_detail'),
    path('tag/<int:tag_id>/', tag_detail, name= 'tag_detail'),
    path('tags/', tag_list, name='tag_list'),
    path('tag_create/', tag_create, name='tag_create'),
    path('post_create/', post_create, name='post_create')
]