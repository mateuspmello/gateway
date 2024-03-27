from rest_framework import serializers
from .models import Author,Post

class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Author
        fields = ['name','email']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(view_name='author-detail', read_only=True)
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']