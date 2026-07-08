from django.contrib import admin
from .models import hero,skills,experience,education,project
# Register your models here.
admin.site.register(hero)
admin.site.register(skills)
admin.site.register(experience)
admin.site.register(education)
admin.site.register(project)