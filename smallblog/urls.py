from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('new_post/', views.create_post, name='create_post'),
    path('salve_post/', views.salve_post, name='salve_post'),
    path('edit_post/<int:id_post>', views.edit_post, name='edit_post'),
    path('save_edit/<int:id_post>', views.salve_edit, name='salve_edit'),
    path('delete_post/<int:id_post>', views.delete_post, name='delete_post'),
]