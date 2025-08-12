from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (  # Исправлено: list_display с маленькой буквы
        "name",
        "created_at",
    )  # Перечисляем поля, отображаемые в таблице списка статей

    search_fields = ["name", "body"]

    list_filter = (
        ("created_at", DateFieldListFilter),  # Дата без времени (используется DateFieldListFilter)
    )  # Перечисляем поля для фильтрации
