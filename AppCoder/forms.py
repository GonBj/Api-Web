from django import forms

class Curso_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()
    
class Alumnos_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    camada = forms.IntegerField()
    curso = forms.CharField(max_length=40)
    email = forms.EmailField()
    
class Profesores_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    camada = forms.IntegerField()
    curso = forms.CharField(max_length=40)
    
    
    
    