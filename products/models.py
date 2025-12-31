from django.db import models
from brands.models import Brand
from categories.models import Category


class Product(models.Model):
    title = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')  # Importando de categories e protegendo
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products')
    description = models.TextField(null=True, blank=True)
    serie_number = models.CharField(max_length=200, null=True, blank=True)
    cost_price = models.DecimalField(max_digits=20, decimal_places=2)  # Uso de Decimal para compor moedas
    selling_price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)  # registro somente da criação
    updated_at = models.DateTimeField(auto_now=True)  # registro de updates

    class Meta:
        ordering = ['title']
# ordenado por nome, poderia ser -name, para ordem invertida, ou  created_at, para ordem por entrada "-" para inverter

    def __str__(self):
        return self.title
