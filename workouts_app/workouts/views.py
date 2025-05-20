from django.shortcuts import render, redirect, get_object_or_404
from .models import Workout
from .forms import WorkoutForm


def workout_list(request):
    workouts = Workout.objects.all()
    return render(request, "workouts/workout_list.html", {"workouts": workouts})


def workout_add(request):
    if request.method == "POST":
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("workout_list")
    else:
        form = WorkoutForm()
    return render(request, "workouts/workout_form.html", {"form": form, "action": "Add"})


def workout_edit(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == "POST":
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect("workout_list")
    else:
        form = WorkoutForm(instance=workout)
    return render(request, "workouts/workout_form.html", {"form": form, "action": "Edit"})


def workout_delete(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == "POST":
        workout.delete()
        return redirect("workout_list")
    return render(request, "workouts/workout_confirm_delete.html", {"workout": workout})
