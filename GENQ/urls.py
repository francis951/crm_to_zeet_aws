"""
URL configuration for GENQ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from GENQapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
     # C (Create)
    path('', views.form_data, name='form_data'),
    #R (Reads)
    path('data/', views.data_read, name='data_read'),
    #Update
    path('<int:id>/', views.form_data, name='update_data'),
    # D (Delete)
    path('data_delete/<str:candidate_id>/', views.data_delete, name='data_delete'),
]
