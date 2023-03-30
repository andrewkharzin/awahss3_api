from django.urls import path, include
from apps.profiles.models import Profile
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Profile
        fields = [
            'id',
            'user', 
            'first_name', 
            'second_name', 
            'last_name', 
            'position', 
            'phone', 
            'shift_work',
            'birthday',
            'private_account',
            'followers',
            'following',
            'panding_request',
            'blocked_user',
            'created_date',
            'avatar', 
            ]

    def get_birthday(self, obj):
            return obj.birthday.strftime("%d-%m-%Y")

class EachUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.email')
    class Meta:
        model = Profile
        fields = ('id','user','first_name', 'second_name', 'last_name', 'position', 'phone', 'shift_work',)
        read_only_fields = ('id','position', 'phone', 'shift_work',)

class FollowerSerializer(serializers.ModelSerializer):
    followers = EachUserSerializer(many=True, read_only= True)
    following = EachUserSerializer(many=True,read_only=True)
    
    class Meta:
        model = Profile
        fields = ('followers','following')
        read_only_fields = ('followers','following')

class BlockPendinSerializer(serializers.ModelSerializer):
    panding_request = EachUserSerializer(many=True, read_only= True)
    blocked_user = EachUserSerializer(many=True,read_only=True)

    class Meta:
        model = Profile
        fields = ('panding_request','blocked_user')  
        read_only_fields = ('panding_request','blocked_user')