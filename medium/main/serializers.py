from .models import *
from rest_framework import serializers
from taggit.models import Tag
# from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

# from main import documents as articles_documents


# class PostDocumentSerializer(DocumentSerializer):
#     class Meta:
#         document = articles_documents.PostDocument
#         fields = (
#             'id',
#             'title',
#             'body',
#             'author',
#             'created',
#             'modified',
#             'pub_date',
#         )
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        depth = 1


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 1


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        depth = 1
