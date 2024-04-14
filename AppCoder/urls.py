from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name="Home"),
    path("ver_cursos", views.ver_cursos, name="Cursos"),
    #path("alta_curso/<nombre>", views.alta_curso),
    path("alummos", views.alumnos, name="alumnos"),
    path("alta_curso", views.curso_formulario),
    path("buscar_curso", views.buscar_curso),
    path("buscar", views.buscar),
    path("elimina_curso/<int:id>", views.elimina_curso, name="elimina_curso"),
    path("editar_curso/<int:id>", views.editar, name="editar_curso"),
    
    path("alta_alumno", views.alumno_formulario),
    path("buscar_alumno", views.buscar_alumno),
    path("busqueda_alumno", views.busqueda_alumno),
    path("ver_alumnos", views.ver_alumnos, name="Alumnos"),
    path("eliminar_alumno/<int:id>", views.eliminar_alumno, name="eliminar_alumno"),
    path("editar_alumno/<int:id>", views.editar_alumno, name="editar_alumno"),
    
    path("alta_profesor", views.profesor_formulario),
    path("ver_profesores", views.ver_profesores, name="Profesores"),
    path("buscar_profesor", views.buscar_profesor),
    path("busqueda_profesor", views.busqueda_profesor),
    path("eliminar_profesor/<int:id>", views.eliminar_profesor, name="eliminar_profesor"),
    path("editar_profesor/<int:id>", views.editar_profesor, name="editar_profesor"),
    
    path("login", views.login_request , name="Login"),
    path("register", views.register, name="Register"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path("editarPerfil" , views.editarPerfil , name="editarPerfil")
    
]