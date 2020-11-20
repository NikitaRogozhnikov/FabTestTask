from django.contrib import admin
from .models import Question, Answer, Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display=('title','end_date',)



admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Choice)
# Register your models here.
