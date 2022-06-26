# ==============================================================================
# PYTHON IMPORTS
# ==============================================================================
from django.db import models
from django.utils import timezone


# ==============================================================================
# CLASSES (inherits from Model)
# ==============================================================================
class LogMessage(models.Model):
    message = models.CharField(max_length=100)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"
