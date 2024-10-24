from django.urls import path
from . import views  # Импорт модуля views из текущего приложения

app_name = 'gallery'  # Определение имени приложения для использования в шаблонах и URL-маршрутах

urlpatterns = [  # Определение списка URL-маршрутов для приложения
    path('', views.index, name='index'),  # Определение маршрута для главной страницы
    path('select_genre/', views.select_genre, name='select_genre'),  # Определение маршрута для выбора жанра
    path('select_theme/', views.select_theme, name='select_theme'),  # Определение маршрута для выбора темы
]