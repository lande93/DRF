
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post
from .models import Rating,Postviewed




class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'content','post_image','created_on','updated_on']




       ## For Comment Serializer
from .models import Comment

class PostSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'comments']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'username','email','comment_body', 'post','status','created','likes','dislikes']


    # For Category Serializer

from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'posts']

class PostSerializer(serializers.ModelSerializer):
   # owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'comments', 'categories','created_on','updated_on','post_image','comments']


class RatingSerializer(serializers.ModelSerializer):
    total_rating = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = Rating
        fields = ['id', 'post', 'ratings','total_rating','rating_owner']

class PostSerializer(serializers.ModelSerializer):
    ratings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'comments', 'categories','created_on','updated_on','post_image','ratings',
                  'post_views']



 # Postviewed
class PostviewedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Postviewed
        fields = ['id', 'post']


class PostSerializer(serializers.ModelSerializer):
    total_rating = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_on', 'updated_on','owner', 'post_image','total_rating','categories','status']


