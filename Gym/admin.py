from django.contrib import admin
from .models import Questions,Choice

admin.site.site_header = "Daily Gym Tracker"
admin.site.site_title = "Personal Gym tracker"



# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    fields = ['Gymworkout']
    inlines = [ChoiceInline]


admin.site.register(Questions,QuestionAdmin)