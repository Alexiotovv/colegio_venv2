from django.shortcuts import render
from colegio.Apps.Aulas.models import Aulas
from datetime import *

def Aulas(request):
    ano_actual = Aulas.objects.get(Ano=datetime.now().year)
    aulas= Aulas.objects.filter(AnoAcademico=ano_actual)
    return render(request,{'aulas':aulas})