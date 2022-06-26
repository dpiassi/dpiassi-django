# ==============================================================================
# PYTHON IMPORTS
# ==============================================================================
import re

# ==============================================================================
# DJANGO IMPORTS
# ==============================================================================
from django.contrib.auth.models import User, Group
from django.utils.timezone import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView

# ==============================================================================
# REST FRAMEWORK IMPORTS
# ==============================================================================
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin
)
from rest_framework.viewsets import GenericViewSet

# ==============================================================================
# EMPLOYEE APP IMPORTS
# ==============================================================================
from employee_app.forms import LogMessageForm, EmployeeForm
from employee_app.models import LogMessage, Employee
from employee_app.serializers import EmployeeSerializer, UserSerializer, GroupSerializer

# ==============================================================================
# TERMINAL LOGS
# ==============================================================================
print("http://127.0.0.1:8000/admin")
print("http://127.0.0.1:8000/home")
print("http://127.0.0.1:8000/hello/VSCode")
print()


# ==============================================================================
# LIST VIEW
# ==============================================================================
class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['employee_list'] = Employee.objects.all()
        return context


# ==============================================================================
# VIEW SETS
# ==============================================================================
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployeeViewSet(GenericViewSet,  # generic view functionality
                      CreateModelMixin,  # handles POSTs
                      RetrieveModelMixin,  # handles GETs for 1 Object
                      ListModelMixin,  # handles GETs for many Objects
                      DestroyModelMixin  # handles DELETEs for 1 Object
                      ):
    """
    API endpoint that allows employees to be viewed or edited.
    """
    queryset = Employee.objects.all().order_by("-updated_at")
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class=None


# ==============================================================================
# FUNCTIONS
# ==============================================================================

def about(request):
    return render(request, "employee_app/about.html")


def contact(request):
    return render(request, "employee_app/contact.html")


def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "employee_app/log_message.html", {"form": form})


def new_employee(request):
    form = EmployeeForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()
            return redirect("home")
    else:
        return render(request, "employee_app/new_employee.html", {"form": form})


def hello_there(request, name):
    return render(
        request,
        'employee_app/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
