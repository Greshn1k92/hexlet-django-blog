from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse


class IndexView(View):
    def get(self, request, tag, article_id):
        context = {
            'article_id': article_id,
            'tag': tag
        }
        return render(request, 'articles/index.html', context)


class HomeRedirectView(View):
    def get(self, request):
        # Генерируем URL по имени маршрута
        url = reverse('article', kwargs={'tag': 'python', 'article_id': 42})
        # Перенаправляем на этот URL
        return redirect(url)

