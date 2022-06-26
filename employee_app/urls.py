# ==============================================================================
# DJANGO IMPORTS
# ==============================================================================
from django.urls import include, path

# ==============================================================================
# REST FRAMEWORK IMPORTS
# ==============================================================================
from rest_framework import routers

# ==============================================================================
# EMPLOYEE APP IMPORTS
# ==============================================================================
from employee_app import views
from employee_app.models import LogMessage, Employee


# ==============================================================================
# PUBLIC OBJECTS
# ==============================================================================

"""
ListView to display the newest logged messages
"""
home_list_view = views.HomeListView.as_view(
    # :5 limits the results to the five most recent
    queryset=LogMessage.objects.order_by("-log_date")[:5],
    context_object_name="message_list",
    template_name="employee_app/home.html",
)

"""
REST Framework Router
"""
router = routers.DefaultRouter(trailing_slash=True)
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"employee", views.EmployeeViewSet)


# ==============================================================================
# PUBLIC LISTS
# ==============================================================================

# API paths:
urlpatterns = [
    # Wire up our API using automatic URL routing.
    path("", include(router.urls)),

    # Additionally, we include login (auth) URLs for the browsable API.
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework"))
]

# Front-End paths:
urlpatterns += [
    path("home/", home_list_view, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("log/", views.log_message, name="log"),
    path("new_employee/", views.new_employee, name="new_employee"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
