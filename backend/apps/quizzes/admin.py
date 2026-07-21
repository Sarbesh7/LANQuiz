from django.contrib import admin
from .models import Category, Quiz, Option ,Question
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at", "updated_at")
    search_fields = ("name", "description")
    ordering = ("name",)

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "description", "time_per_question", "is_active", "created_at", "updated_at")
    search_fields = ("title", "description")
    list_filter = ("category", "is_active")
    ordering = ("title",)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("quiz", "text", "order", "created_at", "updated_at")
    search_fields = ("text",)
    list_filter = ("quiz",)
    ordering = ("quiz", "order")

  
@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ("question", "text", "is_correct", "order", "created_at", "updated_at")
    search_fields = ("text",)
    list_filter = ("is_correct",)
    ordering = ("question", "order")
