from distutils.errors import CompileError
from lzma import CHECK_SHA256
from django import forms
from .models import User, Movie, Role, Actor, Vote, Comment


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'type', 'name', 'lastName', 'phone', 'country', 'zip')

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'image', 'description', 'budget')

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ('name', 'image', 'description', 'age', 'ethnicity', 'category')

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ('name', 'videoFile', 'image', 'resume')

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)
