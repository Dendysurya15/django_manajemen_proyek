from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("tambah_proyek",views.tambah_proyek,name="tambah_proyek"),
    path("tambah_progress/<int:id>",views.tambah_progress,name="tambah_progress"),
    path("insert_new_progress/<int:id>",views.insert_new_progress,name="insert_new_progress"),
    path("edit_progress_tugas/<int:id>",views.edit_progress_tugas,name="edit_progress_tugas"),
    path("update_progress_tugas/<int:id>",views.update_progress_tugas,name="update_progress_tugas"),
    path("delete_progress_tugas/<int:id>",views.delete_progress_tugas,name="delete_progress_tugas"),
    path("update/<int:id>",views.updateData,name="updateData"),
    path("insert",views.insertData,name="insertData"),
]