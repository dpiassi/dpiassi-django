# ==============================================================================
# DJANGO IMPORTS
# ==============================================================================
from django.urls import path

# ==============================================================================
# EMPLOYEE APP IMPORTS
# ==============================================================================
from employee_app import views
from employee_app.models import LogMessage


# ==============================================================================
# PUBLIC OBJECTS
# ==============================================================================
home_list_view = views.HomeListView.as_view(
    # :5 limits the results to the five most recent
    queryset=LogMessage.objects.order_by("-log_date")[:5],
    context_object_name="message_list",
    template_name="employee_app/home.html",
)


# ==============================================================================
# PUBLIC LISTS
# ==============================================================================
urlpatterns = [
    path("", home_list_view, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("log/", views.log_message, name="log"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
