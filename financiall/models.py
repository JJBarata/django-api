from django.db import models

class Receita(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255, unique_for_month='data')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    class Meta:
        db_table = 'receitas'
    
    def __str__(self):
        return self.descricao

class Despesa(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255, unique_for_month='data')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    class Meta:
        db_table = 'despesas'
    
    def __str__(self):
        return self.descricao

