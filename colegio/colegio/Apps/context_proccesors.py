from colegio.Apps.AnoAcademico.models import AnoAcademico
#este archivo se agrega en settings
def data_templates(request):
    ###Obteniendo Año Escolar
    ano=AnoAcademico.objects.filter().order_by('-id')[0]
    return {'ano':ano}