#!/usr/bin/env python
import os
import sys
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hexlet_django_blog.settings')
django.setup()

from hexlet_django_blog.article.models import Article

def create_articles():
    # Статья 1
    article1 = Article.objects.create(
        name="Введение в Django",
        body="Django - это высокоуровневый веб-фреймворк для Python, который позволяет быстро создавать безопасные и масштабируемые веб-приложения."
    )
    print(f"Создана статья: {article1.name}")

    # Статья 2
    article2 = Article.objects.create(
        name="Основы Python",
        body="Python - это интерпретируемый язык программирования высокого уровня, который известен своей простотой и читаемостью."
    )
    print(f"Создана статья: {article2.name}")

    # Статья 3
    article3 = Article.objects.create(
        name="Веб-разработка",
        body="Веб-разработка включает в себя создание веб-сайтов и веб-приложений с использованием различных технологий и языков программирования."
    )
    print(f"Создана статья: {article3.name}")

    # Статья 4
    article4 = Article.objects.create(
        name="Базы данных",
        body="Базы данных - это организованные коллекции данных, которые позволяют эффективно хранить, извлекать и управлять информацией."
    )
    print(f"Создана статья: {article4.name}")

    # Статья 5
    article5 = Article.objects.create(
        name="API и REST",
        body="REST API - это архитектурный стиль для создания веб-сервисов, который использует HTTP методы для взаимодействия с ресурсами."
    )
    print(f"Создана статья: {article5.name}")

    print(f"\nВсего создано статей: {Article.objects.count()}")

if __name__ == '__main__':
    create_articles()
