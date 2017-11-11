# Python imports
# Django imports
from django.db import models
from django.contrib.auth.models import User
# Third-Party imports
# Apps imports

class HomeOwner(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User)

    class Meta:
        verbose_name = "Homeowner"
        verbose_name_plural = "Homeowners"
        get_latest_by = "created_at"
        ordering = ['id', ]

    def __str__(self):
        return "{}".format(self.user)

    def __repr__(self):
        return "{}".format(self.user)
