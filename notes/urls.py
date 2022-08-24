from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_note, name="list"),
    path('delete/<int:pk>', views.delete_note, name="delete"),
    path('addnote/', views.add_note, name="add"),
    path('edit/<int:pk>', views.edit_note, name="edit"),
]