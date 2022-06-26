# ==============================================================================
# PYTHON IMPORTS
# ==============================================================================
import re

# ==============================================================================
# DJANGO IMPORTS
# ==============================================================================
from django.utils.timezone import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView

# ==============================================================================
# EMPLOYEE APP IMPORTS
# ==============================================================================
from employee_app.forms import LogMessageForm
from employee_app.models import LogMessage


# ==============================================================================
# TERMINAL LOGS
# ==============================================================================
print("http://127.0.0.1:8000/log")
print("http://127.0.0.1:8000/hello/VSCode")
print()


# ==============================================================================
# CLASSES
# ==============================================================================
class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context


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


def hello_there(request, name):
    return render(
        request,
        'employee_app/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )


# ==============================================================================
# UNUSED (LEGACY)
# ==============================================================================
def hello_there_without_html_templates(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%a, %d %b, %y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)
