# Python imports
# Django imports
from django.contrib.auth.models import User
# Third-Party imports
# Apps imports
from myproject.apps.homeowners.models import HomeOwner

def create_object_homeowner(email, password):
    return HomeOwner(
        user=User.objects.create_user(email, email, password)
    )
