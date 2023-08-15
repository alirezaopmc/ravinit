from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    student_id = models.CharField(
        max_length=20,
        unique=True,
    )
    first_name = models.CharField(
        max_length=32,
        blank=False,
    )
    last_name = models.CharField(
        max_length=32,
        blank=False,
    )
    photo = models.ImageField(upload_to='photos')


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Course(models.Model):
    name = models.CharField(max_length=32, unique=True)
    students = models.ManyToManyField(
        Student,
    )

    def __str__(self):
        return f'{self.name}'

class Score(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
    )
    value = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(20)],
        blank=False,
        decimal_places=2,
        max_digits=4,
        null=False,
    )

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f'{self.course}:{self.value}'