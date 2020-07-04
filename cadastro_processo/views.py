from django.shortcuts import render
import csv, io
from django.contrib import messages

# Create your views here.
from principal.models import Processo


def upload(request):

    template = "cadastro_processo/home.html"
    data = Processo.objects.all()

    prompt = {
        'order' : 'Ordem do CSV: pasta, comarca, uf'
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    arquivo_csv = request.FILES['arquivo']

    if not arquivo_csv.name.endswith('.csv'):
        messages.error(request, 'ARQUIVO INVALIDO!')

    data_set = arquivo_csv.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for coluna in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Processo.objects.update_or_create(
            pasta=coluna[0],
            comarca=coluna[1],
            uf=coluna[2]
        )

    context = {}
    return  render(request, template, context)
