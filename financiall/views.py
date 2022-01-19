from rest_framework import viewsets
from financiall.models import Receita, Despesa
from financiall.serializer import ReceitaSerializer, DespesaSerializer


class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer

class DespesaViewSet(viewsets.ModelViewSet):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
