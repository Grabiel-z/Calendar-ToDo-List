from django.contrib import admin
from .models import Task, Subtask, Team, Tag, Comment


admin.site.register(Task)
admin.site.register(Subtask)
admin.site.register(Team)
admin.site.register(Tag)
admin.site.register(Comment)
