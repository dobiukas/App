from django.contrib import admin
from .models import Food, Profile, PostFood, forum, Discussion


class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Food)
admin.site.register(Profile)
admin.site.register(PostFood)

###
admin.site.register(forum)
admin.site.register(Discussion)