
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Habit

class HabitListAPI(APIView):
    def get(self, request):
        habits = Habit.objects.all()
        data = [{'id':h.id,'name':h.name} for h in habits]
        return Response(data)
