from django.db import migrations


def add_example_workouts(apps, schema_editor):
    workout = apps.get_model('workouts', 'Workout')
    example_data = [
        ("Morning Run", "cardio", "medium"),
        ("Evening Yoga", "flexibility", "low"),
        ("HIIT Session", "cardio", "high"),
        ("Strength Circuit", "strength", "high"),
        ("Core Workout", "strength", "medium"),
        ("Balance Training", "balance", "low"),
        ("Pilates Class", "flexibility", "medium"),
        ("Sprint Intervals", "cardio", "high"),
        ("Full Body Workout", "strength", "medium"),
        ("Stretching Routine", "flexibility", "low"),
    ]

    for name, workout_type, intensity in example_data:
        workout.objects.create(name=name, workout_type=workout_type, intensity=intensity)


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_example_workouts),
    ]
