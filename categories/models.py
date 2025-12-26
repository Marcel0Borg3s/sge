from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=500)  # campo obrigatório
    description = models.TextField(null=True, blank=True)  # campo não obrigatório
    created_at = models.DateTimeField(auto_now_add=True)  # registro somente da criação
    updated_at = models.DateTimeField(auto_now=True)  # registro de updates

    class Meta:
        ordering = ['name']
# ordenado por nome, poderia ser -name, para ordem invertida, ou  created_at, para ordem por entrada "-" para inverter

    def __str__(self):
        return self.name
# aqui o __str__ garante o reotno da pesquisa em nome listado e não em um número do bd garantindo a fácil visulização quando consultado
