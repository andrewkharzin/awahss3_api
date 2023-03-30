from django.urls import path, include
from apps.users.models import User
from apps.notes.models import Note, NoteShares, Collection, Tag, Category
from rest_framework import routers, serializers, viewsets
from api.apps.users.serializers import UserSerializer
from rest_framework_recursive.fields import RecursiveField


# Serializers define the API representation.

# class RecursiveField(serializers.Serializer):
#     def to_representation(self, value):
#         serializer = self.parent.parent.__class__(value, context=self.context)
#   
#       return serializer.data

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__',

class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class CategorySerializer(serializers.ModelSerializer):
    parent = RecursiveField(many=True)
    class Meta:
        model = Category
        fields=('id', 'name', 'parent',)


class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collection
        fields = ['get_bookmark_url',]

class NoteSerializer(serializers.HyperlinkedModelSerializer):
    # parent = RecursiveField(many=True, required=False)
    category = serializers.StringRelatedField(many=False)
    author = serializers.StringRelatedField(many=False)
    obj = serializers.StringRelatedField(many=False)
    class Meta:
        model = Note
        fields = ['id', 'category',  'obj', 'author', 'title', 'content', 'share_to', 'createAt', 'updateAt', ]


class NoteSharesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NoteShares
        fields = ['id', 'owner', 'title', 'shared_with', 'parent',]\

