from re import T
from django.shortcuts import render
from .forms import UserForm, MovieForm, RoleForm, ActorForm, VoteForm, CommentForm

# Create your views here.
from django.shortcuts import render, redirect
from .models import User, Movie, Role, Actor, Vote, Comment
from django.http import JsonResponse

def user_list(req):
    users = User.objects.all().order_by('name')
    return render(req, 'spotlight/user_list.html', {'users': users})
def user_details(request, pk):
    user = User.objects.get(id=pk)
    data = {'id': user.id, 'email': user.email, 'password': user.password, 'type': user.type, 'name': user.name, 'lastName': user.lastname, 'phone': user.phone, 'country': user.country, 'zip': user.zip}
    return JsonResponse(data, safe=False)
def user_create(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_details', pk=user.pk)
    else:
        form = UserForm()
    return render(req, 'spotlight/user_form.html', {'form': form})
def user_edit(req, pk):
    user = User.objects.get(pk=pk)
    if req.method == "POST":
        form = UserForm(req.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('user_details', pk=user.pk)
    else:
        form = UserForm(instance=user)
    return render(req, 'spotlight/user_form.html', {'form': form})
def user_delete(req, pk):
    User.objects.get(id=pk).delete()
    return redirect('user_list')


def movie_list(req):
    movies = Movie.objects.all().order_by('name')
    return render(req, 'spotlight/movie_list.html', {'movies': movies})
def movie_details(req, pk):
    movie = Movie.objects.get(id=pk)
    return render(req, 'spotlight/movie_details.html', {'movie': movie})
def movie_create(req):
    if req.method == 'POST':
        form = MovieForm(req.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movie_details', pk=movie.pk)
    else:
        form = MovieForm()
    return render(req, 'spotlight/movie_form.html', {'form': form})
def movie_edit(req, pk):
    movie = Movie.objects.get(pk=pk)
    if req.method == "POST":
        form = MovieForm(req.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movie_details', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(req, 'spotlight/movie_form.html', {'form': form})
def movie_delete(req, pk):
    Movie.objects.get(id=pk).delete()
    return redirect('movie_list')


def role_list(req):
    roles = Role.objects.all().order_by('name')
    return render(req, 'spotlight/role_list.html', {'roles': roles})
def role_details(req, pk):
    role = Role.objects.get(id=pk)
    return render(req, 'spotlight/role_details.html', {'role': role})
def role_create(req):
    if req.method == 'POST':
        form = RoleForm(req.POST)
        if form.is_valid():
            role = form.save()
            return redirect('role_details', pk=role.pk)
    else:
        form = RoleForm()
    return render(req, 'spotlight/role_form.html', {'form': form})
def role_edit(req, pk):
    role = Role.objects.get(pk=pk)
    if req.method == "POST":
        form = RoleForm(req.POST, instance=role)
        if form.is_valid():
            role = form.save()
            return redirect('role_details', pk=role.pk)
    else:
        form = RoleForm(instance=role)
    return render(req, 'spotlight/role_form.html', {'form': form})
def role_delete(req, pk):
    Role.objects.get(id=pk).delete()
    return redirect('role_list')


def actor_list(req):
    actors = Actor.objects.all().order_by('name')
    return render(req, 'spotlight/actor_list.html', {'actors': actors})
def actor_details(req, pk):
    actor = Actor.objects.get(id=pk)
    return render(req, 'spotlight/actor_details.html', {'actor': actor})
def actor_create(req):
    if req.method == 'POST':
        form = ActorForm(req.POST)
        if form.is_valid():
            actor = form.save()
            return redirect('actor_details', pk=actor.pk)
    else:
        form = ActorForm()
    return render(req, 'spotlight/actor_form.html', {'form': form})
def actor_edit(req, pk):
    actor = Actor.objects.get(pk=pk)
    if req.method == "POST":
        form = ActorForm(req.POST, instance=actor)
        if form.is_valid():
            actor = form.save()
            return redirect('actor_details', pk=actor.pk)
    else:
        form = ActorForm(instance=actor)
    return render(req, 'spotlight/actor_form.html', {'form': form})
def actor_delete(req, pk):
    Actor.objects.get(id=pk).delete()
    return redirect('actor_list')


def vote_list(req):
    votes = Vote.objects.all()
    return render(req, 'spotlight/vote_list.html', {'votes': votes})
def vote_details(req, pk):
    vote = Vote.objects.get(id=pk)
    return render(req, 'spotlight/vote_details.html', {'vote': vote})
def vote_create(req):
    if req.method == 'POST':
        form = VoteForm(req.POST)
        if form.is_valid():
            vote = form.save()
            return redirect('vote_details', pk=vote.pk)
    else:
        form = VoteForm()
    return render(req, 'spotlight/vote_form.html', {'form': form})
def vote_delete(req, pk):
    Vote.objects.get(id=pk).delete()
    return redirect('vote_list')


def comment_list(req):
    comments = Comment.objects.all()
    return render(req, 'spotlight/comment_list.html', {'comments': comments})
def comment_details(req, pk):
    comment = Comment.objects.get(id=pk)
    return render(req, 'spotlight/comment_details.html', {'comment': comment})
def comment_create(req):
    if req.method == 'POST':
        form = CommentForm(req.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_details', pk=comment.pk)
    else:
        form = CommentForm()
    return render(req, 'spotlight/comment_form.html', {'form': form})
def comment_edit(req, pk):
    comment = Comment.objects.get(pk=pk)
    if req.method == "POST":
        form = CommentForm(req.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_details', pk=comment.pk)
    else:
        form = CommentForm(instance=comment)
    return render(req, 'spotlight/comment_form.html', {'form': form})
def comment_delete(req, pk):
    Comment.objects.get(id=pk).delete()
    return redirect('comment_list')