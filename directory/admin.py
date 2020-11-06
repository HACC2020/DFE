from django.contrib import admin
from .models import usergroups
from .models import applications
from .models import projects
from .models import percents

# Register your models here.
admin.site.register(usergroups)
admin.site.register(applications)
admin.site.register(projects)
admin.site.register(percents)
