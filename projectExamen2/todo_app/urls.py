from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_todo, name='create_todo'),
    path('update/<int:pk>/', views.update_todo, name='update_todo'),
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),

    path('list/ids/', views.list_ids, name='list_ids'),
    path('list/id-titles/', views.list_id_titles, name='list_id_titles'),
    path('list/unresolved/', views.list_unresolved, name='list_unresolved'),
    path('list/resolved/', views.list_resolved, name='list_resolved'),
    path('list/id-user/', views.list_id_user, name='list_id_user'),
    path('list/resolved-user/', views.list_resolved_user, name='list_resolved_user'),
    path('list/unresolved-user/', views.list_unresolved_user, name='list_unresolved_user'),
]
