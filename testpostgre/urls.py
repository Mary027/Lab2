"""
URL configuration for testpostgre project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings  # Импорт настроек Django
from django.conf.urls.static import static  # Импорт функции static для обслуживания статических файлов в режиме разработки
from django.urls import include, path  # Импорт функций include и path для определения маршрутов URL

urlpatterns = [  # Определение списка URL-маршрутов для проекта
    path('admin/', admin.site.urls),  # Определение маршрута для административной панели Django
    path('', include('app.urls')),  # Определение маршрута для включения URL-маршрутов из приложения 'app'
]
