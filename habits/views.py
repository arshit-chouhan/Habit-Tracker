
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta
from .models import Habit, HabitLog
from .forms import HabitForm

@login_required
def dashboard(request):
    habits = Habit.objects.filter(user=request.user)
    today = date.today()

    for habit in habits:
        HabitLog.objects.get_or_create(habit=habit, date=today)

    logs = HabitLog.objects.filter(habit__user=request.user, date=today)

    return render(request, 'habits/dashboard.html', {'logs': logs})


@login_required
def add_habit(request):
    if request.method == "POST":
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('dashboard')
    else:
        form = HabitForm()

    return render(request, 'habits/add_habit.html', {'form': form})


@login_required
def toggle_habit(request, log_id):
    log = HabitLog.objects.get(id=log_id)
    log.completed = not log.completed
    log.save()
    return redirect('dashboard')


@login_required
def habit_detail(request, habit_id):
    habit = Habit.objects.get(id=habit_id)
    today = date.today()

    logs = []
    for i in range(30):
        day = today - timedelta(days=i)
        log, created = HabitLog.objects.get_or_create(habit=habit, date=day)
        logs.append(log)

    logs.reverse()

    return render(request, 'habits/detail.html', {'habit': habit, 'logs': logs})


@login_required
def edit_habit(request, habit_id):
    habit = Habit.objects.get(id=habit_id)
    if request.method == "POST":
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = HabitForm(instance=habit)

    return render(request, 'habits/add_habit.html', {'form': form})


@login_required
def delete_habit(request, habit_id):
    habit = Habit.objects.get(id=habit_id)
    habit.delete()
    return redirect('dashboard')
