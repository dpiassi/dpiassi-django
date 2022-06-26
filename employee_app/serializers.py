# ==============================================================================
# DJANGO IMPORTS
# ==============================================================================
from django.contrib.auth.models import User, Group

# ==============================================================================
# REST FRAMEWORK IMPORTS
# ==============================================================================
from rest_framework import serializers

# ==============================================================================
# EMPLOYEE APP IMPORTS
# ==============================================================================
from employee_app.models import Employee


# ==============================================================================
# SERIALIZERS
# ==============================================================================
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Employee
        exclude = ('url',)
