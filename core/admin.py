from django.contrib import admin
from core.models import Trend, Trainer, Workout, BlogPost, Direction, Feedback, WorkoutProgram, PersonalInfo

admin.site.register(Trend)
admin.site.register(Trainer)
admin.site.register(Workout)
admin.site.register(BlogPost)
admin.site.register(Direction)
admin.site.register(Feedback)
admin.site.register(WorkoutProgram)
admin.site.register(PersonalInfo)

# Register your models here.