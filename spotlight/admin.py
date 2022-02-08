from curses.ascii import US
from django.contrib import admin

# Register your models here.


from .models import User
from .models import Movie
from .models import Role
from .models import Actor
from .models import Vote
from .models import Comment

admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Role)
admin.site.register(Actor)
admin.site.register(Vote)
admin.site.register(Comment)
