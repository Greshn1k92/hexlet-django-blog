from django.views import View
from django.shortcuts import render


class IndexView(View):
    def get(self, request):
        context = {
            'app_name': 'article'
        }
        return render(request, 'articles/index.html', context)
