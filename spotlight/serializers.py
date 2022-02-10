from rest_framework import serializers
from .models import User, Movie, Role, Actor, Vote, Comment

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'type', 'name', 'lastName', 'phone', 'country', 'zip' )

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_details',
        read_only=True
    )

    class Meta:
        model = Movie
        fields = ('id', 'user', 'name', 'image', 'description', 'budget')

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    movie = serializers.HyperlinkedRelatedField(
        view_name='movie_details',
        read_only=True
    )

    class Meta:
        model = Role
        fields = ('id', 'movie', 'name', 'image', 'description', 'age', 'ethnicity', 'category')

class ActorSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_details',
        read_only=True
    )
    role = serializers.HyperlinkedRelatedField(
        view_name='role_details',
        read_only=True
    )

    class Meta:
        model = Actor
        fields = ('id', 'user', 'role', 'name', 'videoFile', 'image', 'resume')

class VoteSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_details',
        read_only=True
    )
    actor = serializers.HyperlinkedRelatedField(
        view_name='actor_details',
        read_only=True
    )

    class Meta:
        model = Vote
        fields = ('id', 'user', 'actor')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_details',
        read_only=True
    )
    movie = serializers.HyperlinkedRelatedField(
        view_name='movie_details',
        read_only=True
    )
    role = serializers.HyperlinkedRelatedField(
        view_name='role_details',
        read_only=True
    )
    actor = serializers.HyperlinkedRelatedField(
        view_name='actor_details',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'user', 'movie', 'role', 'actor', 'message')