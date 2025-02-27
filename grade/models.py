from django.db import models

# Pilihan nilai dan grade point
GRADE_CHOICES = [
    ('A', 4.0),
    ('AB', 3.5),
    ('B', 3.0),
    ('BC', 2.5),
    ('C', 2.0),
    ('D', 1.0),
    ('E', 0.0),
]

class Course(models.Model):
    course_name = models.CharField(max_length=100)  # Nama mata kuliah
    credits = models.PositiveIntegerField()         # SKS
    grade = models.CharField(max_length=2, choices=[(g[0], g[0]) for g in GRADE_CHOICES])

    def __str__(self):
        return f"{self.course_name} ({self.grade})"
