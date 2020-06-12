from django.db import models

class User(models.Model):
    def __str__(self):
        return self.nome
    CURSOS = (
        ('cc','Ciências da computação'),
        ('ds','Design'),
    )
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    #foto = models.ImageField()
    cep = models.CharField(max_length=10)
    curso = models.CharField(
        max_length= 25,
        choices=CURSOS,
    )

