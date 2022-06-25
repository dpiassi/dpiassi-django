import re
from django.utils.timezone import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

print("http://127.0.0.1:8000/hello/VSCode")


def home(request):
    return HttpResponse("Hello, Django!")


def hello_there(request, name):
    return render(
        request,
        'employee_app/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )


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