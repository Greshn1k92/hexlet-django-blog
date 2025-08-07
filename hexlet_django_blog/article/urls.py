from django.urls import path
from .views import IndexView, HomeRedirectView

urlpatterns = [
    path('', HomeRedirectView.as_view(), name='home'),  # Домашняя страница
    path('tags/<str:tag>/<int:article_id>/', IndexView.as_view(), name='article'),
]
