from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View 
from django.views.decorators.csrf import csrf_exempt
from .models import Curso
import json
# Create your views here.

class CursoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            cursos = list(Curso.objects.filter(id=id).values())
            if len(cursos) > 0:
                # Curso = cursos[0]
                datos = {'messagge': "success",'Curso': Curso}
            else:
                datos = {'messagge' : "Curso no encontrado"}
            return JsonResponse(datos)
        else:
            
            cursos = list(Curso.objects.values())
            
            if len(cursos) > 0:
                 datos = {'message':"success",'cursos':cursos}
            else:
                     datos = {'message':"Curso no encontrado...."}
            return JsonResponse(datos)
    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        Curso.objects.create(nombre=jd['nombre'], descripcion=jd['descripcion'],precio=jd['precio'])
        datos={'message':"success"}
        return JsonResponse(datos)
    def put(self, request):
        jd = json.loads(request.body)
        cursos = list(Curso.objects.filter(id=id).values())
        if len(cursos) > 0:
            curso = Curso.objects.get(id=id)
            curso.name = jd['nombre']
            curso.name = jd['descripcion']
            curso.name = jd['precio']
            curso.save()
            datos = {'message':"Success"}
        else:
            datos = {'mesagge'"Curso no encontrado"}
    def delete(self, request):
        pass