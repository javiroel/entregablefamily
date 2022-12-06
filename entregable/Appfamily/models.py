from django.db import models

class family(models.Model):

     nombre=models.CharField(max_length=40)
     vinculo=models.CharField(max_length=40)
     
     def __str__(self):
        return self.nombre+" "+str(self.vinculo)
