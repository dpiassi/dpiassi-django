# ==============================================================================
# DJANGO IMPORTS
# ==============================================================================
from django import forms

# ==============================================================================
# EMPLOYEE APP IMPORTS
# ==============================================================================
from employee_app.models import LogMessage, Employee


# ==============================================================================
# FORMS
# ==============================================================================
class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)   # NOTE: the trailing comma is required


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ("created_at", "updated_at")
