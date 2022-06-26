# ==============================================================================
# DJANGO IMPORTS
# ==============================================================================
from django import forms

# ==============================================================================
# EMPLOYEE APP IMPORTS
# ==============================================================================
from employee_app.models import LogMessage


# ==============================================================================
# CLASSES (inherits from ModelForm)
# ==============================================================================
class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)   # NOTE: the trailing comma is required
