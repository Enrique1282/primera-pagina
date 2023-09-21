from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=200)
    fechaNacimiento = models.DateField()
    edad = models.CharField(max_length=3)
    sexos = (('F','Femenino'), ('M', 'Masculino'))
    sexo = models.CharField(max_length=1, choices=sexos, default='M')
    parentesco = models.CharField(max_length=15)
    def NombreCompleto(self):
        cadena = "{0} {1}"
        return cadena.format(self.nombre, self.apellido, self.parentesco)
    
    def __str__(self):
        return self.NombreCompleto()
    




    # class Meta:
    #     app_label = 'AppF'
    
    # def __str__(self):
    #     return self.cadena
