# ==============================================================================
# DJANGO IMPORTS
# ==============================================================================
from django.db import models
from django.utils import timezone


# ==============================================================================
# CHOICES
# ==============================================================================
DEPARTMENT_CHOICES = [
    ("UND", "Undefined"),
    ("TES", "Tester"),
    ("DEV", "Developer"),
    ("HR", "Human Resources"),
]


# ==============================================================================
# MODELS
# ==============================================================================
class LogMessage(models.Model):
    message = models.CharField(max_length=100)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    department = models.CharField(
        max_length=3,
        choices=DEPARTMENT_CHOICES,
    )

    def first_name(self):
        return str(self.name).split().pop(0)

    def __str__(self):
        """Returns a string representation of an employee."""
        date = timezone.localtime(self.created_at)
        return f"'{self.name}' ({self.email}) added on {date.strftime('%A, %d %B, %Y at %X')}"
