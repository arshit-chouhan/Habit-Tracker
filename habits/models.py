
from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def current_streak(self):
        logs = HabitLog.objects.filter(habit=self, completed=True).order_by('-date')
        streak = 0
        today = date.today()
        for log in logs:
            if log.date == today - timedelta(days=streak):
                streak += 1
            else:
                break
        return streak


class HabitLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField()
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('habit', 'date')


class Reminder(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    reminder_time = models.TimeField()
