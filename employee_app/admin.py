# ==============================================================================
# DJANGO IMPORTS
# ==============================================================================
from django.contrib import admin

# ==============================================================================
# EMPLOYEE APP IMPORTS
# ==============================================================================
from employee_app.models import Employee


# ==============================================================================
# ADMIN MODELS
# ==============================================================================
# https://docs.djangoproject.com/en/3.1/ref/contrib/admin/

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'department')
