from django.shortcuts import render
from AppCoder.models import Curso, Alumnos, Profesores
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario, Alumnos_formulario, Profesores_formulario
from django.contrib import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.


def inicio(request):
    return render(request , "padre.html")


def alta_curso(request,nombre):
    curso = Curso(nombre=nombre, camada=234512)
    curso.save()
    texto = f'Se guardo en la BD el curso: {curso.nombre} {curso.camada}'
    return HttpResponse(texto)

def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos" : cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def alumnos(request):
    return render(request, "alumnos.html")


def curso_formulario(request):
    if request.method == "POST":
        
       mi_formulario = Curso_formulario(request.POST)
       
       if mi_formulario.is_valid():
           datos = mi_formulario.cleaned_data
           
           curso = Curso(nombre=datos["nombre"], camada=datos["camada"])
           curso.save()
           return render(request , "formulario.html")
   
    return render(request , "formulario.html")


def buscar_curso(request):
    return render(request, "buscar_curso.html")

def buscar(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]

        cursos = Curso.objects.filter(nombre__icontains= nombre)

        return render( request , "resultado_busqueda.html" , {"cursos":cursos})

    else:

        return HttpResponse("Ingrese el nombre del curso")
    


def elimina_curso(request , id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    
    curso = Curso.objects.all()
    
    return render(request , "cursos.html" , {"cursos":curso})


def editar(request , id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()
            curso = Curso.objects.all()
            return render(request , "cursos.html" , {"cursos":curso})

        
    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre , "camada":curso.camada})
    
    return render( request , "editar_curso.html" , {"mi_formulario": mi_formulario , "curso":curso})





#------------------- TERCERA ENTREGA------------------ #


def alta_alumno(request, nombre, apellido, camada, curso, email):
    alumno = Alumnos(nombre=nombre, apellido=apellido, camada=camada, curso=curso, email=email)
    alumno.save()
    texto = f'Se guardó en la BD el alumno: {alumno.nombre} {alumno.apellido} {alumno.camada} {alumno.curso} {alumno.email}'
    return HttpResponse(texto)


def alumno_formulario(request):
    if request.method == "POST":
        
       formulario = Alumnos_formulario(request.POST)
       
       if formulario.is_valid():
           datos = formulario.cleaned_data
           
           alumno = Alumnos(nombre=datos["nombre"], apellido=datos["apellido"], camada=datos["camada"], curso=datos["curso"], email=datos["email"],)
           alumno.save()
           return render(request , "formulario_de_alumnos.html")
   
    return render(request , "formulario_de_alumnos.html")



def buscar_alumno(request):
    return render(request, "buscar_alumno.html")



def busqueda_alumno(request):
    

    if "nombre" in request.GET and "apellido" in request.GET:

        nombre = request.GET["nombre"]
        apellido = request.GET["apellido"]

        alumnos = Alumnos.objects.filter(nombre__icontains= nombre, apellido__icontains=apellido)

        return render( request , "result_busqueda_alumno.html" , {"alumnos":alumnos})

    else:

        return HttpResponse("Ingrese el nombre del alumno")
    
    
def ver_alumnos(request):
    alumnos = Alumnos.objects.all()
    dicc = {"alumnos": alumnos}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def eliminar_alumno(request , id):
    alumno = Alumnos.objects.get(id=id)
    alumno.delete()
    
    alumno = Alumnos.objects.all()
    
    return render(request , "alumnos.html" , {"alumnos":alumno})


def editar_alumno(request , id):
    alumno = Alumnos.objects.get(id=id)
    if request.method == "POST":
        formulario = Alumnos_formulario( request.POST )
        if formulario.is_valid():
            datos = formulario.cleaned_data
            alumno.nombre = datos["nombre"]
            alumno.apellido = datos["apellido"]
            alumno.camada = datos["camada"]
            alumno.curso = datos["curso"]
            alumno.email = datos["email"]
            alumno.save()
            alumno = Alumnos.objects.all()
            return render(request , "alumnos.html" , {"alumnos":alumno})

        
    else:
        formulario = Alumnos_formulario(initial={"nombre":alumno.nombre , "apellido":alumno.apellido, "camada":alumno.camada , "curso":alumno.curso, "email":alumno.email})
    
    return render( request , "editar_alumno.html" , {"formulario": formulario , "alumno":alumno})


##---Profesores---##

def alta_profesor(request, nombre, apellido, camada, curso):
    profesor = Profesores(nombre=nombre, apellido=apellido, camada=camada, curso=curso)
    profesor.save()
    texto = f'Se guardó en la BD el alumno: {profesor.nombre} {profesor.apellido} {profesor.camada} {profesor.curso}'
    return HttpResponse(texto)


def profesor_formulario(request):
    if request.method == "POST":
        
       formulario = Profesores_formulario(request.POST)
       
       if formulario.is_valid():
           datos = formulario.cleaned_data
           
           profesor = Profesores(nombre=datos["nombre"], apellido=datos["apellido"], camada=datos["camada"], curso=datos["curso"])
           profesor.save()
           return render(request , "formulario_de_profesores.html")
   
    return render(request , "formulario_de_profesores.html")

def ver_profesores(request):
    profesores = Profesores.objects.all()
    dicc = {"profesores": profesores}
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def buscar_profesor(request):
    return render(request, "buscar_profesor.html")



def busqueda_profesor(request):
    

    if "nombre" in request.GET and "apellido" in request.GET:

        nombre = request.GET["nombre"]
        apellido = request.GET["apellido"]

        profesores = Profesores.objects.filter(nombre__icontains= nombre, apellido__icontains=apellido)

        return render( request , "result_busqueda_profesor.html" , {"profesores":profesores})

    else:

        return HttpResponse("Ingrese el nombre del profesor")
    
    
def eliminar_profesor(request , id):
    profesor = Profesores.objects.get(id=id)
    profesor.delete()
    
    profesor = Profesores.objects.all()
    
    return render(request , "profesores.html" , {"profesores":profesor})


def editar_profesor(request , id):
    profesor = Profesores.objects.get(id=id)
    if request.method == "POST":
        formulario = Profesores_formulario( request.POST )
        if formulario.is_valid():
            datos = formulario.cleaned_data
            profesor.nombre = datos["nombre"]
            profesor.apellido = datos["apellido"]
            profesor.camada = datos["camada"]
            profesor.curso = datos["curso"]
            profesor.save()
            profesor = Profesores.objects.all()
            return render(request , "profesores.html" , {"profesores":profesor})
        
    else:
        formulario = Profesores_formulario(initial={"nombre":profesor.nombre , "apellido":profesor.apellido, "camada":profesor.camada , "curso":profesor.curso})
    
    return render( request , "editar_profesor.html" , {"formulario": formulario , "profesor":profesor})


def login_request(request):
    if request.method == "POST":
        pass
    
    form = AuthenticationForm()
    return render( request, "login.html" , {"form":form})