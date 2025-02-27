from django.contrib import admin
from .models import lead, Agent, User

# Register your models here.
admin.site.register(lead)
admin.site.register(Agent)
admin.site.register(User)