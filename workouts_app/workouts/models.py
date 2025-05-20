from django.db import models


class Workout(models.Model):
    WORKOUT_TYPE_CHOICES = [
        ('cardio', 'Cardio'),
        ('strength', 'Strength'),
        ('flexibility', 'Flexibility'),
        ('balance', 'Balance'),
    ]

    INTENSITY_LEVEL_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    name = models.CharField(max_length=100, verbose_name="Workout Name")
    workout_type = models.CharField(
        max_length=20,
        choices=WORKOUT_TYPE_CHOICES,
        verbose_name="Type"
    )
    intensity = models.CharField(
        max_length=6,
        choices=INTENSITY_LEVEL_CHOICES,
        verbose_name="Intensity"
    )

    def __str__(self):
        return f"{self.name} ({self.get_workout_type_display()} - {self.get_intensity_display()})"
