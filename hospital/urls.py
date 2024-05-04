"""
URL configuration for hospital project.

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
from django.urls import path

from clinic.views import *



from clinic.views import patient_list
from clinic.views import ward_list



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), 
    path('patient/', Patients, name='Patients'),
    path('ward/', Wards, name='Wards'),
    path('about.html', about, name='about'),
    path('home.html', home, name='home'), 
    path('doctors.html', doctors, name='doctors'),
    path('services.html', services, name='services'),
    path('ward/about.html', about, name='about'),
    path('ward/home.html', home, name='home'),
    path('patient/home.html', home, name='home'),
    path('patient/about.html', about, name='about'),
    path('viewwards/', viewwards, name='viewwards'),
    path('viewpatients/', viewpatients, name='viewpatients'),
    path('viewpatients/home.html', home, name='home'),
    path('viewpatients/about.html', about, name='about'),
    path('viewwards/home.html', home, name='home'),
    path('viewwards/about.html', about, name='about'),

    path('viewpatients/', patient_list, name='viewpatients'),
    path('viewward/', ward_list, name='viewward'),

    path('editpatient/<str:patient_id>/', editpatient, name='editpatient'),
    path('editward/<str:ward_id>/', editward, name='editward'),
    path('delete/<str:patient_id>/', delete_patient, name='delete_patient'),
    path('delete_ward/<str:ward_id>/', delete_ward, name='delete_ward'),
]