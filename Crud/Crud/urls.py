"""Crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from tasks import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name='home'),
    path("admin/", admin.site.urls),
    path("signup/", views.signup, name='signup'),
    path("tasks/", views.tasks, name='tasks'),
    path("tasks_completed/", views.tasks_completed, name='tasks_completed'),
    path("tasks/create/", views.task_create, name='create_task'),
    path("tasks/<int:task_id>", views.task_detail, name='task_detail'),
    path("tasks/<int:task_id>/complete", views.task_save, name='task_complete'),
    path("tasks/<int:task_id>/delete", views.task_delete, name='task_delete'),
    path("logout/", views.sigout, name='logout'),
    path("signin/", views.signin, name='signin'),
    path('chat/', include('chat.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
