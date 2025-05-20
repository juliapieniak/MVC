from django import forms
from .models import Workout


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ["name", "workout_type", "intensity"]
