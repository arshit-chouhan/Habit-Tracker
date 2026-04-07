
from django.contrib import admin
from .models import Habit, HabitLog, Reminder

admin.site.register(Habit)
admin.site.register(HabitLog)
admin.site.register(Reminder)
