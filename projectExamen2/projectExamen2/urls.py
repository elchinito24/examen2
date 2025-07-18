from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include('todo_app.urls')),
    path('', lambda request: redirect('list_id_titles')),  # redirige / a /todos/list/id-titles/
]
