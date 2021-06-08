from django.contrib import admin

from .models import Choices, Questions


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Tetx Info',               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Questions, QuestionAdmin)
admin.site.register(Choices)