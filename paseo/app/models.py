from django.db import models



class User(models.Model):
    def __str__(self):
        return self.nome
    CURSOS = (
        ('Ciências da computação','Ciências da computação'),
        ('Design','Design'),
    )
    nome = models.CharField(max_length=100)
    #foto = models.ImageField()
    email = models.EmailField()
    endereco = models.CharField(max_length=200)
    placa = models.CharField(max_length=8)
    cep = models.CharField(max_length=50)
    curso = models.CharField(
        max_length= 25,
        choices=CURSOS,

    )



