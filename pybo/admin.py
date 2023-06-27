from django.contrib import admin
from .models import Question
from .models import Answer


admin.site.register(Answer)

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)

# Register your models here.
