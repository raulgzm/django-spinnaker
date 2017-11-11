# Python imports
# Django imports
from django.contrib import admin
# Third-Party imports
# Apps imports
from .models import HomeOwner

class HomeOwnerAdmin(admin.ModelAdmin):
    pass

admin.site.register(HomeOwner, HomeOwnerAdmin)
