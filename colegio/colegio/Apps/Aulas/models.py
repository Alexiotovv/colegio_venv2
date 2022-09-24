from django.db import models
from colegio.Apps.Grado.models import Grado
from colegio.Apps.Seccion.models import Seccion
from colegio.Apps.AnoAcademico.models import AnoAcademico

class Aulas(models.Model):
    Grado=models.ForeignKey(Grado,null=False,blank=False,on_delete='CASCADE')
    Seccion=models.ForeignKey(Seccion,null=False,blank=False,on_delete='CASCADE')
    AnoAcademico=models.ForeignKey(AnoAcademico,null=False,blank=False,on_delete='CASCADE')