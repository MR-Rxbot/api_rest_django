from django.urls import path
from .views import CursoView


urlpatterns=[
    path('Curso/', CursoView.as_view(),name='cursos_list'),
    path('Curso/<int:id>', CursoView.as_view(),name='cursos_process')
]