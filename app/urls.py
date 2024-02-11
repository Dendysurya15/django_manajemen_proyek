"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from tugas import views as tugas_views
from proyek import views as proyek_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("proyek.urls")),
    
    path("edit_proyek/<int:proyek_id>", proyek_url.edit_proyek, name='edit_proyek'),
    path("delete_proyek/<int:id>", proyek_url.deleteData, name='delete_proyek'),
    path('view_tugas/<int:proyek_id>', tugas_views.view_tugas, name='view_tugas'),
]
