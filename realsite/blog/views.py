from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Rating, Postviewed, Category
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Rating
from .serializers import RatingSerializer
from django.db.models import Avg
from rest_framework.views import APIView
import requests
from rest_framework import status
"""
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

"""



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.likes += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.dislikes += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class PostCountByOwnerView(generics.RetrieveAPIView):
    serializer_class = serializers.PostSerializer

    def retrieve(self, request, *args, **kwargs):
        owner_name= self.kwargs['owner_name']
        post_count = Post.objects.filter(owner=owner_name).count()
        return Response({'owner_name': owner_name, 'post_count': post_count})





class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.likes += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.dislikes += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # views.py





class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.PostSerializer



class RatingList(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = serializers.RatingSerializer



class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = serializers.RatingSerializer





class PostTotalRating(APIView):
    def get(self, request, post_id):
        total_rating = Rating.objects.filter(post=post_id).aggregate(Avg('ratings'))['ratings__avg']
        return Response({'total_rating': total_rating})
class PostviewedList(generics.ListCreateAPIView):
    queryset = Postviewed.objects.all()
    serializer_class = serializers.PostviewedSerializer
class PostviewedDetail(generics.RetrieveDestroyAPIView):
    queryset = Postviewed.objects.all()
    serializer_class = serializers.PostviewedSerializer

    def retrieve(self, request,pk= Post.id, *args, **kwargs):
        instance = self.get_object()
        #instance.content_views += 1
        instance.pk += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



def nodejs_view(request):
    response = requests.get('http://localhost:3000')

    if response.status_code== 200:
        data =response.json()
        return data
    else:
        return None

